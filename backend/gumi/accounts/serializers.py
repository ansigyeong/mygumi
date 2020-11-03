from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework import serializers
from .models import VisitCheck

from rest_auth.utils import import_callable
from allauth.account import app_settings as allauth_settings
from allauth.utils import (email_address_exists,
                            get_username_max_length)
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from allauth.socialaccount.helpers import complete_social_login
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.providers.base import AuthProcess

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'nickname',
            'email',
            'profile_image'
        ]

class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitCheck
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)

    def validate_email(self, email):
        return email
    
    def validate_password(self, password):
        return password
    
    def get_cleaned_data(self):
        return {
            'password': self.validated_data.get('password', ''),
            'email': self.validated_data.get('email', '')
        }
    
    def save(self, request):
        user = get_user_model()
        cleand_data = self.get_cleaned_data()
        user.create_user(**cleand_data)
        return user

class RegisterSerializer(serializers.Serializer):
    nickname = serializers.CharField(required=True)
    email = serializers.EmailField(required=settings.ACCOUNT_EMAIL_REQUIRED)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate_nickname(self, nickname):
        nickname = get_adapter().clean_username(nickname)
        return nickname

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if email and email_address_exists(email):
            raise serializers.ValidationError(
                "A user is already registered with this e-mail address.")
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(_("The two password fields didn't match."))
        return data
    
    def get_cleaned_data(self):
        return {
            'nickname': self.validated_data.get('nickname', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', '')
        }
    
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.nickname = request.data.get('nickname')
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])

        return user