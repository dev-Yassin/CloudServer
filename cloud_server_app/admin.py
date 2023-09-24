from django.contrib import admin
from .models import Device, File

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'device']
