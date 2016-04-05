import random
from django import template 

from apps.blog.views import get_object_or_None

from apps.spider.models import Calendar

register = template.Library()


@register.inclusion_tag('index/right/calendars.html')
def get_calendar_list():
    cals = Calendar.objects.order_by('?')[:10]
    return {'cals': cals}


@register.inclusion_tag('destination/destinations_list.html')
def get_destinations_list():
    pass
