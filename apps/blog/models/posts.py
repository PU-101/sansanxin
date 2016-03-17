from django.db import models
from django.contrib.auth.models import User
from . import MyPostManager


# 发布条目
class Post(models.Model):
	user = models.ForeignKey(User)
	content = models.CharField(max_length=280, blank=True)
	picture = models.ImageField()
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

	views_num = models.PositiveIntegerField(default=1)
	likes_hum = models.PositiveIntegerField(default=0)
	comments_num = models.PositiveIntegerField(default=0)

	objects = models.Manager()
	my_post_manager = MyPostManager()

	def clean(self):
		pass

	class Meta():
		ordering = ['-created_at']

	def __str__(self):
		return self.user.username+'--'+self.content