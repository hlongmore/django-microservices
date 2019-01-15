from django.contrib import admin

from .models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')

# Assume the site already installs the user and group models.
admin.site.register(Service, ServiceAdmin)
