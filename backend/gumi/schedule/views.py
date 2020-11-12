# Create your views here.
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
# Create your views here.

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes
from django.contrib.auth import get_user_model
from .models import Schedule
from .serializers import ScheduleSerializer,ScheduleCreateSerializer
# from .permissions import Permission
from django.conf import settings
from accounts.models import CustomUser
from tour.models import Place
from .permissions import SchedulePermission
from accounts.serializers import UserSerializer

from drf_yasg.utils import swagger_auto_schema

User = get_user_model()

class ScheduleView(APIView):

    permission_classes =[SchedulePermission]

    def get(self, request,user_id):
        # schedule_pk : 0 이면 전체 스케줄 목록 조회 1 이상이면 특정 스케줄 조회
        schedule = Schedule.objects.filter(user=user_id)
        serializer = ScheduleSerializer(instance=schedule, many=True)
        # print(serializer.data['data']['user'])
        res = {
            'data': serializer.data
        }
        return Response(res,status=status.HTTP_200_OK)

    def post(self, request, user_id):
        # user = get_list_or_404(User,id=user_id)
        data = request.data
        data['host'] = user_id
        data['user'] = [user_id]
        serializer = ScheduleCreateSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class HostView(APIView):

    permission_classes =[SchedulePermission]

    def get(self, request, user_id, schedule_pk):
        schedule = Schedule.objects.filter(id=schedule_pk)
        serializer = ScheduleSerializer(instance=schedule, many=True)
        res = {
            'data': serializer.data
        }
        return Response(res,status=status.HTTP_200_OK)

    def patch(self, request, user_id, schedule_pk):
        schedule = get_object_or_404(Schedule,id=schedule_pk)
        schedule.date = request.data['date']
        schedule.title = request.data['title']
        schedule.save()
        serializer = ScheduleSerializer(instance=schedule)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, user_id, schedule_pk):
        schedule = get_object_or_404(Schedule,id=schedule_pk)
        schedule.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PlaceAddView(APIView):
    permission_classes =[SchedulePermission]

    def post(self, request, schedule_pk):
        schedule = get_object_or_404(Schedule,id=schedule_pk)
        if schedule.host.id == request.user.id:
            places = request.data
            for place in places:
                schedule.place.add(place)
            serializer = ScheduleSerializer(instance=schedule)
            response = {
                'status': True,
                'data': serializer.data,
                'flag': True
            }
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response = {
                'status': False,
                'message': '호스트만 방문 지역 추가가 가능합니다.'
            }
            return Response(response, status=status.HTTP_200_OK)

class PlaceView(APIView):

    permission_classes =[SchedulePermission]

    def delete(self, request, place_id,schedule_pk):
        schedule = get_object_or_404(Schedule,id=schedule_pk)
        if schedule.host.id == request.user.id:
            schedule.place.remove(place_id)
            serializer = ScheduleSerializer(instance=schedule)
            response = {
                'status': True,
                'data': serializer.data,
                'flag': False
            }
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            response = {
                'status': False,
                'message': '호스트만 방문 지역 삭제가 가능합니다.'
            }
            return Response(response, status=status.HTTP_200_OK)   

class InvitedAddView(APIView):
    permission_classes =[SchedulePermission]

    def post(self, request, schedule_pk):
        schedule = get_object_or_404(Schedule,id=schedule_pk)
        if schedule.host.id == request.user.id:
            users = request.data
            for user in users:
                schedule.user.add(user)
            serializer = ScheduleSerializer(instance=schedule)
            response = {
                'status': True,
                'data': serializer.data,
                'flag': True
            }
            return Response(response, status=status.HTTP_201_CREATED)       
        else:
            response = {
                'status': False,
                'message': '호스트만 초대가 가능합니다.'
            }
            return Response(response, status=status.HTTP_200_OK)

class InvitedView(APIView):

    permission_classes =[SchedulePermission]

    def delete(self, request, user_id, schedule_pk):
        schedule = get_object_or_404(Schedule,id=schedule_pk)
        if schedule.host.id == request.user.id:
            schedule.user.remove(user_id)
            serializer = ScheduleSerializer(instance=schedule)
            response = {
                'status': True,
                'data': serializer.data,
                'flag': False
            }
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        else:
            response = {
                'status': False,
                'message': '호스트만 추방이 가능합니다.'
            }
            return Response(response, status=status.HTTP_200_OK)
