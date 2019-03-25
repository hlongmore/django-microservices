from django.contrib import admin

from .models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'command')

    def command(self, obj):
        return obj.command_name if obj.command_name else 'runserver'


# Assume the site already installs the user and group models.
admin.site.register(Service, ServiceAdmin)
