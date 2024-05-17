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

    def get_queryset(self):
        student_id = self.kwargs['pk']
        course_id = self.kwargs['course_id']
        #TODO : implement filter class and filter backend
        queryset = self.queryset.filter(pk=student_id, course_id=course_id)
        return queryset


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
