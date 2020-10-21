from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:user_pk>/', views.UserDetailView.as_view()),
    path('<int:user_pk>/visited/', views.VisitCheckView.as_view()),
]
