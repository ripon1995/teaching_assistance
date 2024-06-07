from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import generics
from django.http import Http404
from django.shortcuts import get_object_or_404
from course.serializers import CourseSerializer, CourseEnrollSerializer, EnrolledCoursesSerializer, \
    StudentListOfEnrolledCourseSerializer, CourseGetSerializer
from user.models import UserModel
from course.models import Course, CourseEnroll
from enum import Enum


class Instructor(Enum):
    NOT_AN_INSTRUCTOR = "not an instructor"
    NOT_FOUND_INSTRUCTOR = "not found instructor"


def is_valid_instructor(serializer):
    try:
        instructor = get_object_or_404(UserModel, id=serializer.data.get("course_instructor"))
    except Http404:
        return Instructor.NOT_FOUND_INSTRUCTOR

class CourseCreateView(generics.CreateAPIView):
    def create(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        serializer = CourseSerializer(data=data)

        if not serializer.is_valid():
            instructor = is_valid_instructor(serializer)
            if instructor == Instructor.NOT_FOUND_INSTRUCTOR:
                return Response("Not found instructor")

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


class CourseRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Course.objects.all()

    def retrieve(self, request, *args, **kwargs):
        course = self.get_object()
        serializer = CourseGetSerializer(course)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        course = self.get_object()
        serializer = CourseSerializer(course, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer