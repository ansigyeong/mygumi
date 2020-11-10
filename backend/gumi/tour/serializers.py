from rest_framework import serializers

from .models import Place, Mission, CustomMission, SearchRecord
from review.models import Review, ReviewImage

class ReviewImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewImage
        fields = ['picture']

class ReviewSerializer(serializers.ModelSerializer):
    images = ReviewImageSerializer(many=True, read_only=True)
    class Meta:
        model = Review
        fields = ['id', 'title', 'content', 'comments', 'images', 'user', 'created_at', 'updated_at', 'place']

class PlaceSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()
    class Meta:
        model = Place
        fields = '__all__'
    def get_reviews(self, instance):
        review_get = Review.objects.filter(place=instance).order_by('created_at')
        review_serializer = ReviewSerializer(instance=review_get, many=True)
        return review_serializer.data

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