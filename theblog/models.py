from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=255, null=True)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField(null=True)

    def __str__(self):
        return f"Title : {self.title} - Author : {self.author}"

    def get_absolute_url(self):
        #return reverse("article-detail", args=(str(self.id)))
        return reverse("home")