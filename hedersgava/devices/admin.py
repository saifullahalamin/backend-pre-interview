from django.contrib import admin
from .models import Device


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'unit', )


admin.site.register(Device, DeviceAdmin)
