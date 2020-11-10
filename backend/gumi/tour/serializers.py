from rest_framework import serializers

from .models import Place, Mission, CustomMission, SearchRecord

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

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

class SearchRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchRecord
        fields = ['search']