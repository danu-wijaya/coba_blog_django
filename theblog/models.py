from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255, null=True)
    title_tag = models.CharField(max_length=255, default="My Blog")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField(null=True)

    def __str__(self):
        return f"Title : {self.title} - Author : {self.author}"
