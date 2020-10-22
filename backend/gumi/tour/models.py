from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL

class Place(models.Model):
    course = models.IntegerField()
    place = models.CharField(max_length=30)
    image = models.ImageField()
    content = models.TextField()

class Mission(models.Model):
    place = models.ForeignKey(Place,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField()

class CustomMission(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    place = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    content = models.TextField()   