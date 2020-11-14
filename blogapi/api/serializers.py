from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.models import BaseUserManager
from rest_framework import serializers
from .models import Post,Profile


class blogserializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields ='__all__'

class profileserializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields ='__all__'


User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    """
    A user serializer for registering the user
    """

    class Meta:
        model = User
        fields = ('id','username' ,'email', 'password', 'first_name', 'last_name')

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value