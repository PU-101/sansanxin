from django.db import models


# Create your models here.
class Calendar(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=140)
    img_src = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=False, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    class Meta():
    	ordering = ['-created_at']

    def __str__(self):
        return self.title
