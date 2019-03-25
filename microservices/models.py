from django.db import models


class Service(models.Model):
    """A service registry for the services in the cluster."""
    name = models.CharField(max_length=32, help_text='User-friendly service name')
    url = models.CharField(max_length=256, null=True, blank=True,
                           help_text='Not required if running locally')
    local = models.BooleanField(default=True,
                                help_text='Check if running locally')
    active = models.BooleanField(default=True)
    manage = models.CharField(max_length=256, unique=True,
                              help_text="Full path to the directory that the project's manage.py "
                                        "file is in")
    settings = models.CharField(max_length=256, unique=False,
                                help_text="Relative path to the project's settings.py file")
    command_name = models.CharField(max_length=256, null=True, blank=True,
                                    help_text='manage.py command to run if not "runserver"')
    virtual_env = models.CharField(max_length=256, null=True, blank=True,
                                   help_text="Full path to the directory that your virtual "
                                             "environment's bin directory is in")
