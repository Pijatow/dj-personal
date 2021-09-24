from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=3000)
    creation_time = models.DateTimeField(auto_now_add=True)
    last_edit_time = models.DateTimeField(auto_now_add=True)
