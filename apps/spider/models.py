from django.db import models

# Create your models here.
class MafengwoModel(models.Model):
	url = models.URLField()
	title = models.CharField(max_length=140)
	image_src = models.URLField()
	created_at = models.DateTimeField(auto_now_add=False, auto_now=False)