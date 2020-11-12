from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .serializers import UserSerializer, VisitSerializer
from .models import VisitCheck
from review.serializers import ReviewSerializer
from review.models import Review

User = get_user_model()

class UserDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get_object(self, user_pk):
        return get_object_or_404(User, pk=user_pk)

    def get(self, request, user_pk):
        user = self.get_object(user_pk)
        userSerializer = UserSerializer(user)

        reviews = Review.objects.filter(user=user).order_by('-id')
        reviewSerializer = ReviewSerializer(instance=reviews, many=True)

        data = {
            'user': userSerializer.data,
            'reviews': reviewSerializer.data
        }
        return Response(data)
    
    @swagger_auto_schema(request_body=UserSerializer)
    def patch(self, request, user_pk):
        user = self.get_object(user_pk)
        serializer = UserSerializer(instance=user, data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
        return Response(serializer.data)

class VisitCheckView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, user_pk):
        visits = VisitCheck.objects.filter(user=user_pk)
        visitSerializer = VisitSerializer(instance=visits, many=True)

        data = {
            'visited': visitSerializer.data,
        }
        return Response(data)
    
    @swagger_auto_schema(request_body=VisitSerializer)
    def post(self, request, user_pk):
        place = request.data['place']
        user = get_object_or_404(User, id=user_pk)
        if request.user != user:
            return Response('본인이 아닙니다')
        visit = VisitCheck()
        visit.place = place
        visit.user = request.user
        visit.check = 1
        visit.save()
        visits = VisitCheck.objects.filter(user=user_pk)
        visitSerializer = VisitSerializer(instance=visits, many=True)   
        data = {
            'visited': visitSerializer.data,
        }
        return Response(data)
    
    @swagger_auto_schema(request_body=VisitSerializer)
    def patch(self, request, user_pk):
        place = request.data['place']
        user = get_object_or_404(User, pk=user_pk)
        visit = get_object_or_404(VisitCheck, user=user, place=place)
        visit.check = 0
        visit.save()
        visits = VisitCheck.objects.filter(user=user_pk)
        visitSerializer = VisitSerializer(instance=visits, many=True)   
        data = {
            'visited': visitSerializer.data,
        }
        return Response(data)

class UserListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        users = User.objects.all()
        userSerializer = UserSerializer(instance=users, many=True)

        data = {
            'users': userSerializer.data,
        }
        return Response(data)