from rest_framework import serializers

from .models import Place, Mission, CustomMission

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['place','image','content']

class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = ['place','title','content']

class CustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomMission
        fields = ['user','place','title','content']

# class CustomInfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomMission
#         fields = ['user','place','title','content']
