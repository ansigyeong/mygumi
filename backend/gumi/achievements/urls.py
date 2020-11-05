from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:user_pk>/', views.AchievementView.as_view()),
]
