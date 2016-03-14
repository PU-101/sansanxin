from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
	return 'user_{0}/{1}'.format(instance.user.username, filename)


def default_portrait():
	return 'default/default_portrait.jpg'


def create_profile_handler(sender, instance, created, **kwargs):
	if not created:
		return
	profile = models.UserProfile(user=instance)
	profile.save()


# Create your models here.
class UserProfile(models.Model):
	GENDER_CHOICES = (
		('M', '男生'),
		('F', '女生'),
		)
	user = models.OneToOneField(User, primary_key=True)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='F')
	birthday = models.DateField(auto_now_add=False, auto_now=False)
	signature = models.CharField(max_length=40, default='什么都没留下')
	portrait = models.ImageField(upload_to=user_directory_path, default=default_portrait)
	updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

	class Meta():
		ordering = ['created_at']

	def __str__(self):
		return self.user.username