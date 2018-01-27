from django.db import models

# Create your models here.


class Image(models.Model):
    file = models.FileField()
    location = models.CharField(max_length=30)
    caption = models.TextField(max_length=10)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)


class Comment(models.Model):
    content = models.TextField()
    written_at = models.TimeField(auto_now_add=True)
