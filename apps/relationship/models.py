from django.db import models
from django.contrib.auth.models import User
from apps.blog.models import Post


# Create your models here.
class LikeAndStar(models.Model):
	by = models.ForeignKey(User)
	to = models.ForeignKey(Post)
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

	class Meta():
		ordering = ['by']
		abstract = True


class Like(LikeAndStar):
	def __str__(self):
		return '{0}--LIKE--{1}'.format(self.by.username, self.to.content)


class Star(LikeAndStar):
	def __str__(self):
		return '{0}--STAR--{1}'.format(self.by.username, self.to.content)


class Follow(models.Model):
	user1 = models.ForeignKey(User, related_name='by')
	user2 = models.ForeignKey(User, related_name='follow')
	situation = models.IntegerField(default=10)

	def __str__(self):
		return '{0}--FOLLOW--{1}'.format(self.user1.username, self.user2.username)