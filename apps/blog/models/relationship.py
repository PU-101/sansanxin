from django.db import models
from django.contrib.auth.models import User
from . import Post
from . import MyPostManager


class LikeAndStar(models.Model):
	"""
	Like&Star功能
	"""
	by = models.ForeignKey(User)
	to = models.ForeignKey(Post)
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

	class Meta():
		ordering = ['by']
		abstract = True


class Like(LikeAndStar):
	def __str__(self):
		return '{0}--LIKE--{1}'.format(self.by.username, self.to.content)


class Follow(models.Model):
	"""
	Follow功能
	"""
	SITU_CHOICES = (
		('0', 'follow'),
		('1', 'follow each other'),
		)
	user1 = models.ForeignKey(User, related_name='by')
	user2 = models.ForeignKey(User, related_name='follow')
	situation = models.CharField(max_length=1, choices=SITU_CHOICES, default='0')
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

	objects = models.Manager()
	my_post_manager = MyPostManager()

	def __str__(self):
		return '{0}--FOLLOW--{1}'.format(self.user1.username, self.user2.username)


"""
－－－－－－SIGNALS－－－－－－－
"""


# def add_or_cancle_like(delta):
# 	"""
# 	在Like表保存后修改UserProfile中的Likes字段数目
# 	"""
# 	def f(sender, instance, **kwargs):
# 		to_post = instance.to
# 		to_post.likes_num = F('likes_num') + delta
# 		to_post.save()
# 	return f

# add_like = add_or_cancle_like(1)
# post_save.connect(add_like, sender=Like)
# cancle_like = add_or_cancle_like(-1)
# post_delete.connect(cancle_like, sender=Like)


# def add_or_cancle_follow(delta):
# 	"""
# 	同上，修改Follow和Follower字段的数目
# 	"""
# 	def f(sender, instance, **kwargs):
# 		u1 = instance.user1.userprofile
# 		u2 = instance.user2.userprofile
# 		u1.follows_num = F('follows_num') + delta
# 		u1.save()
# 		u2.followers_num = F('followers_num') + delta
# 		u2.save()
# 	return f

# add_follow = add_or_cancle_follow(1)
# post_save.connect(add_follow, sender=Follow)
# cancle_follow = add_or_cancle_follow(-1)
# post_delete.connect(cancle_follow, sender=Follow)