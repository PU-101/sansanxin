from django.db import models
from django.db.models import F
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from . import Post


class Comment(models.Model):
    by = models.ForeignKey(User)
    to = models.ForeignKey(Post)
    reply_to = models.ForeignKey(User, blank=True, null=True, related_name='comment_reply_to')
    content = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta():
        ordering = ['-created_at']

    def __str__(self):
        return self.content


"""
－－－－－－SIGNALS－－－－－－－
"""


def add_or_cancle_comment(delta):
    """
    在Comment表保存后修改Post中的comment_num字段数目
    """
    def f(sender, instance, **kwargs):
        to_post = instance.to
        to_post.comments_num = F('comments_num') + delta
        to_post.save()

    return f

post_save.connect(add_or_cancle_comment(1), sender=Comment)
post_delete.connect(add_or_cancle_comment(-1), sender=Comment)