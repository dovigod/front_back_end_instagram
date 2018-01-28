from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Image(models.Model):
    file = models.FileField()
    location = models.CharField(max_length=30)
    caption = models.TextField(max_length=10)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.location} - {self.caption}'


class Comment(models.Model):
    content = models.TextField()
    created_for = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    written_at = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.written_at}'


class Like(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.TimeField(auto_now_add=True)
    created_for = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.created_for}-{self.created_by}-{self.created_at}'

