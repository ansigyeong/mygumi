from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL

def course_directory_path(instance, filename):
    # instance 는 이 함수를 불러온 table을 의미하게 된다
    # 따라서 instance.course를 가져오면 integerfield로 받아온 값을,
    # instance.course_name을 가져오면 charfield로 받아온 값을 적용한다
    # /media/course/1/filename
    # /media/course/금오산/filename
    return 'course/{}/{}'.format(instance.course_name, filename)

class Place(models.Model):
    course = models.IntegerField()
    course_name = models.CharField(max_length=50)
    place = models.CharField(max_length=30)
    image = models.ImageField(upload_to=course_directory_path)
    content = models.TextField()
    dong = models.CharField(max_length=50)
    time = models.TextField(default='')

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