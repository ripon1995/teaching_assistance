from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from student.models import Student
from student.serailzers import StudentSerializer

class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def create(self, request, *args, **kwargs):
        course_id = self.kwargs.get('course_id')
        request.data['course_id'] = course_id
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)