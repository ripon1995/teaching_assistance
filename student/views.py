from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response

from course.models import Course
from student.models import Student
from student.serailzers import StudentSerializer, StudentRetrieveSerializer, StudentUpdateSerializer, \
    StudentAttendanceListSerializer


class StudentCreateView(generics.CreateAPIView):
    serializer_class = StudentSerializer


class StudentRetrieveView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentRetrieveSerializer

    def retrieve(self, request, *args, **kwargs):
        student_id = self.kwargs.get('student_id')
        course_id = self.kwargs.get('course_id')
        student = Student.objects.filter(pk=student_id, course=course_id).first()
        if student is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StudentUpdateView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentUpdateSerializer


class StudentAttendanceListView(generics.ListAPIView):
    serializer_class = StudentAttendanceListSerializer

    def get_queryset(self):
        course_id = self.kwargs.get('course_id')
        course = get_object_or_404(Course, pk=course_id)
        queryset = Student.objects.filter(course=course)
        return queryset
