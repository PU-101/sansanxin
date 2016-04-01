from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import F
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

def count_likes(instance):
	to_post = instance.to
	likes_num = Like.objects.filter(to=to_post).count()
	to_post.likes_num = likes_num
	to_post.save(update_fields=['likes_num'])

	
@receiver(post_save, sender=Like)
def add_like(sender, instance, created, **kwargs):
	if not created:
		return
	count_likes(instance)


@receiver(post_delete, sender=Like)
def cancle_like(sender, instance, **kwargs):
	count_likes(instance)


def count_follows(instance):
	u1 = instance.user1
	u2 = instance.user2
	u1_follows_num = Follow.objects.filter(user1=u1).count()
	u2_followers_num = Follow.objects.filter(user2=u2).count()
	u1.userprofile.follows_num = u1_follows_num
	u2.userprofile.followers_num = u2_followers_num
	u1.userprofile.save(update_fields=['follows_num'])
	u2.userprofile.save(update_fields=['followers_num'])


@receiver(post_save, sender=Follow)
def add_follow(sender, instance, created, **kwargs):
	if not created:
		return
	count_follows(instance)


@receiver(post_delete, sender=Follow)
def cancle_follow(sender, instance, created, **kwargs):
	count_follows(instance)

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