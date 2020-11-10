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

from .models import Territory, Mission
from .serializers import MissionSerializer, TerritorySerializer

class TrrritoryView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, territory):
        territories = Territory.objects.filter(territory=territory).order_by('?')
        territory = territories[0]
        return territory

    def get(self, request, territory):
        territory = self.get_object(territory)
        territorySerializer = TerritorySerializer(territory)

        data = {
            'territory': territorySerializer.data,
        }
        return Response(data)