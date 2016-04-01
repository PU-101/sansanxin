import re
from django.db import models
from django.contrib.auth.models import User
from . import MyPostManager
from .upload_path import user_directory_path, default_portrait


class Post(models.Model):
	"""
	发布条目
	"""
	user = models.ForeignKey(User)
	commented_by = models.ManyToManyField(User, through='Comment', through_fields=('to', 'by'), related_name='post_commented_by')
	liked_by = models.ManyToManyField(User, through='Like', through_fields=('to', 'by'), related_name='post_liked_by')

	title = models.CharField(max_length=140, blank=True)
	content = models.CharField(max_length=640)
	picture = models.ImageField(upload_to=user_directory_path, default=default_portrait())
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

	views_num = models.PositiveIntegerField(default=1)
	likes_num = models.PositiveIntegerField(default=0)
	comments_num = models.PositiveIntegerField(default=0)

	objects = models.Manager()
	my_post_manager = MyPostManager()

	def clean(self):
		pass
		
	def save(self, *args, **kwargs):
		"""
		若无标题，则取content第一句话作为title
		"""
		if not self.title and not self.content:
			first_sentence = re.split("[,，。.？?；;]", self.content, maxsplit=1)[0]
			if first_sentence:
				self.title = first_sentence + '...'
			else:
				self.title = self.content
		# """
		# 防止出现负数
		# """
		# if self.views_num < 0:
		# 	self.views_num = 0
		# elif self.likes_num < 0:
		# 	self.likes_num = 0
		# elif self.comments_num < 0:
		# 	self.comments_num = 0

		super(Post, self).save(*args, **kwargs)

	class Meta():
		ordering = ['-created_at']

	def __str__(self):
		return self.user.username+'--'+self.title