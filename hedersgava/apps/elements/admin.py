from django.contrib import admin
from .models import Element


class ElementAdmin(admin.ModelAdmin):
    list_display = ('data', 'device', 'value', )


admin.site.register(Element, ElementAdmin)
