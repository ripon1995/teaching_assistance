from rest_framework.parsers import JSONParser
from rest_framework import generics
from rest_framework.response import Response
from user.serializers import UserSerializer
from user.models import UserModel


class RegisterUserView(generics.CreateAPIView):
    queryset = UserModel.objects.all()

    def create(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
