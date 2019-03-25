import multiprocessing as mp
from multiprocessing import Process
from subprocess import check_output

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management import call_command

from microservices.models import Service

class TermColor:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def run_this_server():
    """Start development server for *this* project."""
    call_command('runserver')


def run_server(venv, manage_dir, url, settings, command_name):
    """Start development server for *another* django project."""
    if not venv:
        venv = '/usr'
    if not command_name:
        command_name = 'runserver'
    try:
        py_command = f'{venv}/bin/python'
        manage_command = 'manage.py'
        settings = settings.strip('/')
        if settings.endswith('.py'):
            settings = settings[:-3]
        settings = settings.replace('/', '.')
        django_settings_file = f'--settings={settings}'
        args = [
            py_command,
            manage_command,
            command_name,
            url,
            django_settings_file
        ]
    except Exception as e:
        print(f'Unable to run {e}')
        return
    try:
        check_output(args, cwd=manage_dir)
    except Exception as e:
        command = ' '.join(args)
        print(f'Unable to run {command}:\n{e}')


class Command(BaseCommand):
    help = 'Runserver or other command on all the services in the cluster'

    def handle(self, *args, **options):
        p = Process(target=run_this_server)
        p.start()
        services = Service.objects.filter(local=True, active=True)
        svc_port = 8001
        for count, service in enumerate(services):
            print(f'Service {count}: {service.name}')
            service_url = '127.0.0.1:{}'.format(svc_port) if not service.command_name else ''
            context = mp.get_context(service.start_method)
            p = context.Process(
                target=run_server,
                args=(
                    service.virtual_env,
                    service.manage,
                    service_url,
                    service.settings,
                    service.command_name,
                )
            )
            p.start()
            if not service.command_name or service.command_name == 'runserver':
                self.stdout.write(
                    TermColor.OKGREEN + 'Development server started at http://{0} for: {1}'.format(
                        service.url, service.name) + TermColor.ENDC
                )
                service.url = service_url
                service.save()
                svc_port += 1
            else:
                self.stdout.write(
                    TermColor.OKGREEN + 'Started {0}'.format(service.name) + TermColor.ENDC
                )
            if settings.DEBUG:
                timeout = 20 if not service.command_name else 500
                p.join(timeout)
