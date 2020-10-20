from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.parsers import FileUploadParser
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser

from drf_yasg.utils import swagger_auto_schema

from .models import Review, Comment, ReviewImage
from .serializers import ReviewSerializer, ReviewCreateSerializer, CommentSerializer, CommentCreateSerializer, ReviewImageSerializer
from .permissions import ReViewPermission

# images 업로드 부분은 삭제 가능
# front와 image 표시 관련 협의 후 수정 예정
class ReviewView(APIView):
    parser_class = (FileUploadParser,)
    permission_classes =[ReViewPermission]

    @swagger_auto_schema(request_body=ReviewCreateSerializer)
    def post(self, request):
        """
            # Review를 작성하는 요청
        """
        serializer = ReviewCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            
            # request 로 넘어온 files 중 images 를 모음
            images_data = request.FILES.getlist('images')
            # 이미지 저장 시 사용할 review를 다시 확인
            # serializer를 그대로 사용할 방법을 모르겠음
            review = get_object_or_404(Review, pk=serializer.data['id'])
            for image_data in images_data:
                images = ReviewImage.objects.create(review=review, picture=image_data)
                images.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request):
        queryset = Review.objects.all()
        serializer = ReviewSerializer(instance=queryset, many=True)
        data = {
            'review': serializer.data,
        }
        return Response(data, status=status.HTTP_200_OK)

class ReviewDetailView(APIView):
    permission_classes =[ReViewPermission]

    def get_object(self, review_pk):
        return get_object_or_404(Review, pk=review_pk)
    
    def delete(self, request, review_pk):
        review = self.get_object(review_pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get(self, request, review_pk):
        review = self.get_object(review_pk)
        reviewSerializer = ReviewSerializer(review)

        data = {
            'review': reviewSerializer.data,
        }
        return Response(data)
    
    @swagger_auto_schema(request_body=ReviewCreateSerializer)
    def patch(self, request, review_pk):
        review = self.get_object(review_pk)
        serializer = ReviewCreateSerializer(instance=review, data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
        return Response(serializer.data)

class CommentView(APIView):
    def get(self, request, review_pk):
        review = get_object_or_404(Review, pk=review_pk)
        comments = review.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=CommentCreateSerializer)
    def post(self, request, review_pk):
        review = get_object_or_404(Review, pk=review_pk)
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, review=review)
            return Response(serializer.data)

class CommentDetailView(APIView):

    def delete(self, request, review_pk, comment_pk):
        comment = self.get_object(comment_pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)