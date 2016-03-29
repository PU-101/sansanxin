import re
from django.db import models
from django.contrib.auth.models import User
from . import MyPostManager

"""
发布条目
"""
class Post(models.Model):
	user = models.ForeignKey(User)
	commented_by = models.ManyToManyField(User, through='Comment', through_fields=('to', 'by'), related_name='post_commented_by')
	liked_by = models.ManyToManyField(User, through='Like', through_fields=('to', 'by'), related_name='post_liked_by')

	title = models.CharField(max_length=140, blank=True)
	content = models.CharField(max_length=640)
	picture = models.ImageField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

	views_num = models.PositiveIntegerField(default=1)
	likes_hum = models.PositiveIntegerField(default=0)
	comments_num = models.PositiveIntegerField(default=0)

	objects = models.Manager()
	my_post_manager = MyPostManager()

	def clean(self):
		pass

	"""
	若无标题，则取content第一句话作为title
	"""
	def save(self, *args, **kwargs):
		if not self.title and not self.content:
			first_sentence = re.split("[,，。.？?；;]", self.content, maxsplit=1)[0]
			if first_sentence:
				self.title = first_sentence + '...'
			else:
				self.title = self.content
		super(Post, self).save(*args, **kwargs)

	class Meta():
		ordering = ['-created_at']

	def __str__(self):
		return self.user.username+'--'+self.title