from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers, permissions

# swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# swagger 정보 설정, 관련 엔드포인트 추가
# swagger 엔드포인트는 DEBUG Mode에서만 노출
schema_view = get_schema_view(
    openapi.Info(
        title="GumiTour API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


app_name = 'tour'
urlpatterns = [
    path('<int:course_id>/',views.CourseView.as_view(),name='course'),
    path('place/<int:place_id>/',views.ListView.as_view(),name='list'),
    path('place/<int:place_id>/mission/',views.MissionView.as_view(),name='mission'),
    path('place/<int:user_id>/custom/',views.CustomView.as_view(),name='custom'),
    path('place/<int:user_id>/custom/<int:mission_id>/',views.CustomInfoView.as_view(),name='custominfo'),
    path('search/<int:user_id>/', views.SearchGetView.as_view()),
    path('search/<int:user_id>/<str:dong>/', views.SearchView.as_view()),
    path('review/', include('review.urls')),
    path('admin/', admin.site.urls),
    path('user/', include('accounts.urls')),

    # swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),

    # rest-auth
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/signup/', include('rest_auth.registration.urls')),
]
