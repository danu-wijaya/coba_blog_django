from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Post(models.Model):
    title = models.CharField(max_length=255, null=True)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField(null=True)
    # post_date = models.DateField(auto_now_add=True)
    # post_date = models.DateTimeField(auto_now_add=True)
    post_date = models.DateTimeField(auto_now_add=True,
                                     verbose_name="Post Date",
                                     help_text="Format: dd/mm/yyyy hh:mm")

    def __str__(self):
        return f"Title : {self.title} - Author : {self.author}"

    def get_absolute_url(self):
        # return reverse("article-detail", args=(str(self.id)))
        return reverse("home")
