from rest_framework import serializers

from .models import Place, Mission, CustomMission, SearchRecord
from review.models import Review, ReviewImage

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'nickname',
            'profile_image'
        ]

class ReviewImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewImage
        fields = ['picture']

class ReviewSerializer(serializers.ModelSerializer):
    images = ReviewImageSerializer(many=True, read_only=True)
    create_user = serializers.SerializerMethodField()
    class Meta:
        model = Review
        fields = ['id', 'title', 'content', 'comments', 'images', 'created_at', 'updated_at', 'place', 'create_user']

    def get_create_user(self, instance):
        user_get = get_object_or_404(User, pk = instance.user_id)
        user_serializer = UserSerializer(instance=user_get)
        return user_serializer.data

class PlaceSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()
    class Meta:
        model = Place
        fields = '__all__'
    def get_reviews(self, instance):
        review_get = Review.objects.filter(place=instance).order_by('created_at')
        review_serializer = ReviewSerializer(instance=review_get, many=True)
        return review_serializer.data

class PlaceListSerializer(serializers.ModelSerializer):
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