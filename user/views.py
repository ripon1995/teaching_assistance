from rest_framework.parsers import JSONParser
from rest_framework import generics, status
from rest_framework.response import Response
from user.serializers import UserSerializer, InstructorProfileSerializer, UserProfileSerializer
from user.models import UserModel
from user.model.profile import InstructorProfile


class RegisterUserView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        print(user.pk)
        default_profile_data = {
            'user': user.pk,
        }

        profile_serializer = InstructorProfileSerializer(data=default_profile_data)
        if profile_serializer.is_valid():
            profile = profile_serializer.save()
        else:
            print(profile_serializer.errors)
            user.delete()
            raise ValueError("Failed to create profile")

    def create(self, request, *args, **kwargs):
        user_serializer = self.get_serializer(data=request.data)
        if user_serializer.is_valid():
            self.perform_create(user_serializer)
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response(serializer.data)


class UserProfileRetrieveView(generics.RetrieveAPIView):
    queryset = InstructorProfile.objects.all()
    serializer_class = UserProfileSerializer

    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response(serializer.data)


class ProfileUpdateView(generics.UpdateAPIView):
    queryset = InstructorProfile.objects.all()
    serializer_class = InstructorProfileSerializer

    def partial_update(self, request, *args, **kwargs):
        profile = self.get_object()
        serializer = self.get_serializer(instance=profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
