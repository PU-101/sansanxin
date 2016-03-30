from django import template 
from django.shortcuts import get_object_or_404
from apps.blog.models import UserProfile
from apps.spider.models import Calendar

register = template.Library()


@register.inclusion_tag('left/profile.html')
def get_userprofile_info(user_login):
	user_prof = get_object_or_404(UserProfile, user=user_login)
	return {'user_prof': user_prof}


@register.inclusion_tag('right/calendars.html')
def get_mafengwo_list():
	return {'cals': Calendar.objects.all()[:10]}