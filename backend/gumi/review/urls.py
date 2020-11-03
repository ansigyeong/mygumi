from django.contrib import admin
from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.ReviewView.as_view()),
    path('<int:review_pk>/', views.ReviewDetailView.as_view()),
    path('<int:review_pk>/comment/', views.CommentView.as_view()),
    path('<int:review_pk>/comment/<int:comment_pk>/', views.CommentDetailView.as_view()),
]
