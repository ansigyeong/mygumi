from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
# Create your views here.

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes

from .models import Mission, Place, CustomMission
from .serializers import PlaceSerializer, CustomSerializer, MissionSerializer
from .permissions import Permission

class CourseView(APIView):

    permission_classes = [Permission]

    def get_object(self,course_id):
        return get_list_or_404(Place, course=course_id)

    def get(self, request, course_id):
        place = self.get_object(course_id)
        serializer = PlaceSerializer(instance=place, many=True)
        res = {
            'data': serializer.data
        }
        return Response(res,status=status.HTTP_200_OK)

class ListView(APIView):

    permission_classes = [Permission]

    def get_object(self,place_id):
        return get_object_or_404(Place, pk=place_id)

    def get(self, request, place_id):
        place = self.get_object(place_id)
        serializer = PlaceSerializer(place)
        res = {
            'data' : serializer.data
        }
        return Response(res,status=status.HTTP_200_OK)

class MissionView(APIView):

    permission_classes = [Permission]
    
    def get_object(self, mission_id):
        return get_object_or_404(Mission, pk=mission_id)

    def get(self, request, mission_id):
        mission = self.get_object(mission_id)
        serializer = MissionSerializer(mission)
        res = {
            'data' : serializer.data
        }
        return Response(res,status=status.HTTP_200_OK)

class CustomView(APIView):

    permission_classes = [Permission]

    def get_object(self, user_id):
        return get_list_or_404(CustomMission, user=user_id)

    def get(self, request, user_id):
        custom = self.get_object(user_id)
        serializer = CustomSerializer(instance = custom, many = True)
        res = {
            'data' : serializer.data
        }
        return Response(res,status=status.HTTP_200_OK)

    def post(self, request, user_id):
        data = request.data
        data['user'] = user_id
        serializer = CustomSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class CustomInfoView(APIView):

    permission_classes = [Permission]

    def get_object(self, user_id, mission_id):
        return get_object_or_404(CustomMission, user=user_id, id=mission_id)

    def get(self, request, user_id, mission_id):
        info = self.get_object(user_id,mission_id)
        serializer = CustomSerializer(info)
        res = {
            'data' : serializer.data
        }
        return Response(res,status=status.HTTP_200_OK)

    def delete(self, request, user_id, mission_id):
        info = self.get_object(user_id, mission_id)
        info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, user_id, mission_id):
        info = self.get_object(user_id, mission_id)
        data = request.data
        data['user'] = user_id
        serializer = CustomSerializer(instance = info, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        