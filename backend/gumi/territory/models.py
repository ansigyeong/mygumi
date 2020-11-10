from django.db import models

def course_directory_path(instance, filename):
    return 'territory/{}/{}'.format(instance.territory, filename)

class Territory(models.Model):
    territory = models.CharField(max_length=10)

class Mission(models.Model):
    territory = models.ForeignKey(Territory, on_delete=models.CASCADE)
    content = models.TextField()
    order = models.IntegerField()
    hint = models.TextField()
    answer = models.CharField(max_length=25)
    image = models.ImageField(upload_to=course_directory_path)
