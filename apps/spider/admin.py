from django.contrib import admin
from apps.spider.models import Calendar


class CalendarAdmin(admin.ModelAdmin):
    list_display = ('title', 'destination', 'created_at', 'updated_at')

admin.site.register(Calendar, CalendarAdmin)