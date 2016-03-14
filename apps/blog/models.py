from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
	user = models.ForeignKey(User)
	content = models.CharField(max_length=280, blank=True)
	picture = models.ImageField()
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.user.username+'--'+self.content