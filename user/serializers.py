from rest_framework import serializers

from user.model.profile import InstructorProfile
from user.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['user_name', 'email']


class InstructorProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = InstructorProfile
        fields = ['first_name', 'last_name', 'experience', 'subject', 'user']
