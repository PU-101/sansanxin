import datetime
from django.db import models
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
	portrait = models.ImageField(upload_to=user_directory_path, default=default_portrait())
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

	# def save(self, *args, **kwargs):
	# 	if self.posts_num < 0:
	# 		self.posts_num = 0
	# 	elif self.follows_num < 0:
	# 		self.follows_num = 0
	# 	elif self.followers_num < 0:
	# 		self.followers_num = 0

	# 	super(UserProfile, self).save(*args, **kwargs)

	class Meta():
		ordering = ['created_at']

	def __str__(self):
		return self.user.username