from rest_framework import serializers
from .models import Territory, Mission

class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = '__all__'

class TerritorySerializer(serializers.ModelSerializer):
    missions = serializers.SerializerMethodField()
    class Meta:
        model = Territory
        fields = '__all__'
    def get_missions(self, instance):
        mission_get = Mission.objects.filter(territory=instance).order_by('order')
        mission_serializer = MissionSerializer(instance=mission_get, many=True)
        return mission_serializer.data