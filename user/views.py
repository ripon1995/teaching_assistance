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


class UserRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response(serializer.data)


# class UserLoginView(generics.CreateAPIView):
#     def create(self, request, *args, **kwargs):
#         data = JSONParser().parse(request)
#         email = data.get('email')
#         password = data.get('password')
#         query = UserModel.objects.all().filter(email=email, password=password).first()
#
#         print(query)
#         return Response("User found")
