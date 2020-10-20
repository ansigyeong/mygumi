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

from .serializers import UserSerializer

User = get_user_model()

class UserDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get_object(self, user_pk):
        return get_object_or_404(User, pk=user_pk)

    def get(self, request, user_pk):
        user = self.get_object(user_pk)
        userSerializer = UserSerializer(user)

        data = {
            'user': userSerializer.data,
        }
        return Response(data)
    
    @swagger_auto_schema(request_body=UserSerializer)
    def patch(self, request, user_pk):
        user = self.get_object(user_pk)
        serializer = UserSerializer(instance=user, data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
        return Response(serializer.data)