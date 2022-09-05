from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django_summernote.fields import SummernoteTextField

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
    created_on = models.DateTimeField(auto_now_add=True)
    # likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
