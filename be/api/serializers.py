from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import UserProfile

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    role = serializers.CharField(write_only=True, required=False)  # Allow role assignment

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']

    def create(self, validated_data):
        role_name = validated_data.pop('role', None)  # Extract role if provided
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )

        if role_name:  
            group, created = Group.objects.get_or_create(name=role_name)  # Get or create group
            user.groups.add(group)  # Assign role to user
        
        return user

    def to_representation(self, instance):
        """Include role in the response"""
        rep = super().to_representation(instance)
        rep['role'] = instance.profile.role if hasattr(instance, 'profile') else None
        return rep
        
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile  # Or your actual model
        fields = ["id", "username", "role"]  # Just keep `role`, no `source`


    class Meta:
        model = UserProfile
        fields = ('user', 'role')
