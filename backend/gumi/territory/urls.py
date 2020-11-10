from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'territory'
urlpatterns = [
    path('<str:territory>/',views.TrrritoryView.as_view(),name='course'),
]