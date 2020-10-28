from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL

class Place(models.Model):
    course = models.IntegerField()
    place = models.CharField(max_length=30)
    image = models.ImageField()
    content = models.TextField()
    dong = models.CharField(max_length=10)

class Mission(models.Model):
    place = models.ForeignKey(Place,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField()

class CustomMission(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    place = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    content = models.TextField()   

class SearchRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    search = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)