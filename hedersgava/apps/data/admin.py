from django.contrib import admin

from .models import Data


class DataAdmin(admin.ModelAdmin):
    list_display = ('id', 'record_time', )


admin.site.register(Data, DataAdmin)
