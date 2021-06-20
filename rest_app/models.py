from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth import get_user_model
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
