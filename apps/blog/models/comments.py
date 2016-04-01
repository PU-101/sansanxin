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


