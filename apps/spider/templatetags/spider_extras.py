from django import template 

from apps.spider.models import Calendar

register = template.Library()


@register.inclusion_tag('index/right/calendars.html')
def get_calendar_list(posts_num):
    if posts_num <= 3:
        cals_num = 5
    else:
        cals_num = 10

    # cals = Calendar.objects.order_by('?')[:cals_num]
    cals = Calendar.objects.order_by('-created_at')[:cals_num]
    
    return {'cals': cals}


@register.inclusion_tag('destination/destinations_list.html')
def get_destinations_list():
    pass
