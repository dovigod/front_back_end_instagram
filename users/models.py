from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    avatar = models.FileField()
    bio = models.TextField()
    created_at = models.TimeField(auto_now_add=True)
    update_at = models.TimeField(auto_now=True)
    created_by = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    
    

    def __str__(self):
        return f'{self.created_by}'
