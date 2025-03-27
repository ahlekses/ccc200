from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import UserProfileSerializer
from django.contrib.auth.models import User


from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.shortcuts import render
from .serializers import UserSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username  # Example: Adding a custom claim
        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class UserProfileView(generics.RetrieveAPIView):
    """
    API endpoint that allows users to get their profile information including role
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = UserProfileSerializer
    
    def get_object(self):
        return self.request.user.profile

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]