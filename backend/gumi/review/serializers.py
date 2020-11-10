from rest_framework import serializers

from .models import Review, Comment, ReviewImage
from accounts.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Comment
        fields = '__all__'

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']

class ReviewImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewImage
        fields = ['picture']

class ReviewSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    images = ReviewImageSerializer(many=True, read_only=True)
    class Meta:
        model = Review
        fields = ['id', 'title', 'content', 'comments', 'images', 'user', 'created_at', 'updated_at', 'place']
    def get_comments(self, instance):
        com_get = Comment.objects.filter(review=instance)
        com_serializer = CommentSerializer(instance=com_get, many=True)
        return com_serializer.data

class ReviewCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, read_only=True)
    class Meta:
        model = Review
        fields = ['id', 'title', 'content', 'place']