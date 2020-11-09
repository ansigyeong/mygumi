from django.db import models
from django.conf import settings
from tour.models import Place

User = settings.AUTH_USER_MODEL
# Create your models here.
class Schedule(models.Model):
    place = models.ManyToManyField(Place, related_name='place_day')
    user = models.ManyToManyField(User, related_name='user_schedule')
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=10)