from rest_framework import serializers
from .models import Schedule
from accounts.serializers import UserSerializer
from tour.serializers import PlaceSerializer

class ScheduleSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    host = serializers.SerializerMethodField()
    class Meta:
        model = Schedule
        fields = ['id', 'place','user','host','date','title']
    
    def get_user(self, instance):
        return UserSerializer(instance.user, many=True).data

    def get_host(self, instance):
        return UserSerializer(instance.host).data

    def get_place(self, instance):
        return PlaceSerializer(instance.place, many=True).data

class ScheduleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['user','host','date','title']