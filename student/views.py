from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response

from course.models import Course
from student.models import Student
from student.serailzers import StudentSerializer, StudentRetrieveSerializer, StudentUpdateSerializer


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


class StudentRetrieveView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentRetrieveSerializer

    def retrieve(self, request, *args, **kwargs):
        course_id = self.kwargs.get('course_id')
        course = get_object_or_404(Course, pk=course_id)

        student_id = self.kwargs.get('student_id')
        student = get_object_or_404(Student, pk=student_id, course=course)

        serializer = self.get_serializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StudentUpdateView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentUpdateSerializer

    def partial_update(self, request, *args, **kwargs):
        course_id = self.kwargs.get('course_id')
        course = get_object_or_404(Course, pk=course_id)
        student_id = self.kwargs.get('student_id')
        student = get_object_or_404(Student, pk=student_id, course=course)
        serializer = self.get_serializer(student, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
