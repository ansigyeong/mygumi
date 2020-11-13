from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
# Create your views here.

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes

from .models import Mission, Place, CustomMission, SearchRecord
from .serializers import PlaceSerializer, CustomSerializer, MissionSerializer, SearchRecordSerializer, PlaceListSerializer
from .permissions import Permission

User = get_user_model()

class CourseView(APIView):

    permission_classes = [Permission]

    def get_object(self,course_id):
        return get_list_or_404(Place, course=course_id)

    def get(self, request, course_id):
        place = self.get_object(course_id)
        serializer = PlaceListSerializer(instance=place, many=True)
        res = {
            'data': serializer.data
        }
        return Response(res,status=status.HTTP_200_OK)

    def post(self, request, course_id):
        data = request.data
        data['course'] = course_id
        serializer = PlaceSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

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
    
    def get_place(self, place_id):
        return get_object_or_404(Place, pk=place_id)

    def get(self, request, place_id):
        place = self.get_place(place_id)
        missions = Mission.objects.filter(place = place)
        serializer = MissionSerializer(missions, many = True)
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

class SearchGetView(APIView):
    def get(self, request, user_id):
        searchs = SearchRecord.objects.filter(user=user_id)
        serializer = SearchRecordSerializer(instance=searchs, many=True)
        return Response(serializer.data)

class SearchView(APIView):
    def get(self, request, user_id, dong):
        search_dong = Place.objects.filter(dong__contains=dong)
        search_place = Place.objects.filter(place__contains=dong)
        searchs = search_dong.union(search_place)
        user = get_object_or_404(User, pk=user_id)
        searchSerializer = PlaceListSerializer(instance=searchs, many=True)
        userSearch = SearchRecord.objects.filter(user=user).order_by('created_at')
        check_dong = SearchRecord.objects.filter(user=user, search=dong)
        if len(check_dong) > 0:
            return Response(searchSerializer.data)
        elif len(userSearch) >= 10:
            userSearch[0].delete()
        searchPlus = SearchRecord()
        searchPlus.search = dong
        searchPlus.user = user
        searchPlus.save()
        return Response(searchSerializer.data)

    def delete(self, request, user_id, dong):
        search = get_object_or_404(SearchRecord, user=user_id, search=dong)
        search.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)