import os, datetime

from django.conf import settings
from django.db import models
from django.core.files.base import ContentFile
from django.contrib.auth.models import User
from .upload_path import user_directory_path, default_portrait


# Create your models here.
class UserProfile(models.Model):
	GENDER_CHOICES = (
		('M', '男生'),
		('F', '女生'),
		)
	user = models.OneToOneField(User, primary_key=True)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
	birthday = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
	signature = models.CharField(max_length=40, default='什么都没留下')
	portrait = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
	updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

	posts_num = models.PositiveIntegerField(default=0)
	follows_num = models.PositiveIntegerField(default=0)
	followers_num = models.PositiveIntegerField(default=0)

	@property
	def age(self):
		today = datetime.datetime.today()
		return (today.year - self.birthday.year) - int(
			(today.month, today.day) < (self.birthday.month, self.birthday.day)
			)

	def save(self, *args, **kwargs):
		if not self.portrait:
			def get_default_portrait(gender):
				img_name = '{}.png'.format(gender)
				img_path = os.path.join(settings.STATIC_ROOT, 'blog', default_portrait(gender))
				with open(img_path, 'rb') as f:
					self.portrait.save(img_name, ContentFile(f.read()), save=False)
			
			if self.gender == 'M':
				get_default_portrait('male')
			else:
				get_default_portrait('female')
				
		super(UserProfile, self).save(*args, **kwargs)

	class Meta():
		ordering = ['created_at']

	def __str__(self):
		return self.user.username