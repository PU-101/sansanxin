from django.db import models
from django.contrib.auth.models import User
from . import Post
from . import MyPostManager
from django.db.models.signals import post_save, post_delete
from django.db.models import F


# Create your models here.
class LikeAndStar(models.Model):
	by = models.ForeignKey(User)
	to = models.ForeignKey(Post)

	class Meta():
		ordering = ['by']
		abstract = True


class Like(LikeAndStar):
	def __str__(self):
		return '{0}--LIKE--{1}'.format(self.by.username, self.to.content)


class Follow(models.Model):
	SITU_CHOICES = (
		('0', 'follow'),
		('1', 'follow each other'),
		)
	user1 = models.ForeignKey(User, related_name='by')
	user2 = models.ForeignKey(User, related_name='follow')
	situation = models.CharField(max_length=1, choices=SITU_CHOICES, default='0')

	objects = models.Manager()
	my_post_manager = MyPostManager()

	def __str__(self):
		return '{0}--FOLLOW--{1}'.format(self.user1.username, self.user2.username)

# SIGNALS

# Like Num
def add_like_or_cancle_like(delta):
	def f(sender, instance, **kwargs):
		to_post = instance.to
		to_post.likes = F('likes') + delta
		to_post.save()
	return f

add_like = add_like_or_cancle_like(1)
post_save.connect(add_like, sender=Like)
cancle_like = add_like_or_cancle_like(-1)
post_delete.connect(cancle_like, sender=Like)


# Follow Num
def add_or_cancle_follow(delta):
	def f(sender, instance, **kwargs):
		print('---------------------')
		u1 = instance.user1.userprofile
		u2 = instance.user2.userprofile
		u1.follows = F('follows') + delta
		u1.save()
		u2.followers = F('followers') + delta
		u2.save()
	return f

add_follow = add_or_cancle_follow(1)
post_save.connect(add_follow, sender=Follow)
cancle_follow = add_or_cancle_follow(-1)
post_delete.connect(cancle_follow, sender=Follow)