from rest_framework import serializers

from .models import Place, Mission, Custom

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['place','image','content']

class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        field = ['place_pk','title','content']

class CustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom
        field = ['user_pk','place','title','content']
