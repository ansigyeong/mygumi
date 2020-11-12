from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'calendar'
urlpatterns = [
    path('<int:user_id>/',views.ScheduleView.as_view(),name='course'),
    path('<int:user_id>/<int:schedule_pk>/',views.HostView.as_view(),name='list'),
    path('<int:schedule_pk>/place/',views.PlaceAddView.as_view(),name='mission'),
    path('<int:place_id>/<int:schedule_pk>/place/',views.PlaceView.as_view(),name='mission'),
    path('<int:schedule_pk>/invite/',views.InvitedAddView.as_view(),name='custom'),
    path('<int:user_id>/<int:schedule_pk>/invite/',views.InvitedView.as_view(),name='custom'),

]