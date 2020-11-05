from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Achievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jinpyeong = models.BooleanField(default=False)
    geumosan = models.BooleanField(default=False)
    bicycle = models.BooleanField(default=False)
    seowon = models.BooleanField(default=False)
    explorer = models.BooleanField(default=False)
    korean = models.BooleanField(default=False)