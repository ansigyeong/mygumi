from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='profile/', default='media/default.jpg')

class VisitCheck(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.CharField(max_length=10)
    check = models.IntegerField()