from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework import serializers
from .models import Achievement

User = get_user_model()

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'