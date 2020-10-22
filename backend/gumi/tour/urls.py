from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'tour'
urlpatterns = [
    path('<int:course_id>/',views.CourseView.as_view(),name='course'),
    path('place/<int:place_id>/',views.ListView.as_view(),name='list'),
    path('place/<int:place_id>/mission/',views.MissionView.as_view(),name='mission'),
    path('place/<int:user_id>/custom/',views.CustomView.as_view(),name='custom'),
    path('place/<int:user_id>/custom/<int:mission_id>/',views.CustomInfoView.as_view(),name='custominfo')
]
