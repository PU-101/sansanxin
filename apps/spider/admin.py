from django.contrib import admin
from apps.spider.models import MafengwoModel


class MafengwoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

admin.site.register(MafengwoModel, MafengwoAdmin)