from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
# Create your views here.

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes

from .models import Mission, Place, Custom
from .serializers import PlaceSerializer, CustomSerializer, MissionSerializer
from .permissions import Permission

class Course(APIView):
    permission_classes = [Permission]

    def get_object(self,course_id):
        return get_object_or_404(Place,course = course_id)

    def get(self, request, course_id):
        place = self.get_object(course_id)
        serializer = PlaceSerializer(place)
        res = {
            'data': serializer.data
        }
        return Response(res,status=status.HTTP_200_OK)

class List(APIView):

    def get_object(self,place_id):
        return get_object_or_404(Place,place_id=place_id)

    def get(self, request, place_id):
        place = self.get_object(place_id)
        serializer = PlaceSerializer(place)
        res = {
            'data' : serializer.data
        }
        return Response(res,status=status.HTTP_200_OK)

class Mission(APIView):
    
    def get_object(self, mission_id):
        return get_object_or_404(Mission, mission_id=mission_id)

    def get(self, request, mission_id):
        mission = self.get_object(mission_id)
        serializer = MissionSerializer(mission)
        res = {
            'data' : serializer.data
        }
        return Response(res,status=status.HTTP_200_OK)

class Custom(APIView):

    def get_object(self, user_id):
        return get_object_or_404(Custom, user_pk=user_id)

    def get(self, request, user_id):
        custom = self.get_object(user_id)
        serializer = CustomSerializer(custom)
        res = {
            'data' : serializer.data
        }
        return Response(res,status=status.HTTP_200_OK)

    def post(self, request, user_id):
        serializer = CustomSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
