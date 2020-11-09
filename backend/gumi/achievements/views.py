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

from .models import Achievement
from .serializers import AchievementSerializer
from .permissions import AcheivementPermission

User = get_user_model()

class AchievementView(APIView):
    permission_classes =[AcheivementPermission]

    def get(self, request, user_pk):
        user = get_object_or_404(User, pk=user_pk)
        user_achieve = Achievement.objects.filter(user = user)
        if len(user_achieve) > 0:
            user_achieve = get_object_or_404(Achievement, user=user)
            serializer = AchievementSerializer(user_achieve)
            return Response(serializer.data)
        else:
            user_achieve = Achievement()
            user_achieve.user = user
            user_achieve.save()
            serializer = AchievementSerializer(user_achieve)
            return Response(serializer.data)
    
    @swagger_auto_schema(request_body=AchievementSerializer)
    def patch(self, request, user_pk):
        user_achieve = get_object_or_404(Achievement, user = request.user)
        serializer = AchievementSerializer(instance=user_achieve, data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
        return Response(serializer.data)