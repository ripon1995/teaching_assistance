from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import generics
from django.http import Http404
from django.shortcuts import get_object_or_404
from course.serializers import CourseSerializer, CourseEnrollSerializer, EnrolledCoursesSerializer, \
    StudentListOfEnrolledCourseSerializer
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


def is_instructor(serializer):
    instructor = serializer.validated_data.get('course_instructor')
    if not instructor.is_instructor:
        return Instructor.NOT_AN_INSTRUCTOR
    return instructor


class CourseCreateView(generics.CreateAPIView):
    def create(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        serializer = CourseSerializer(data=data)

        if not serializer.is_valid():
            instructor = is_valid_instructor(serializer)
            if instructor == Instructor.NOT_FOUND_INSTRUCTOR:
                return Response("Not found instructor")

        if serializer.is_valid():
            instructor = is_instructor(serializer)
            print(instructor)
            if instructor == Instructor.NOT_AN_INSTRUCTOR:
                return Response("Not an instructor")
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


class CourseRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Course.objects.all()

    def retrieve(self, request, *args, **kwargs):
        course = self.get_object()
        serializer = CourseSerializer(course)
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


class CourseListViewOfSingleInstructor(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def list(self, request, *args, **kwargs):
        instructor_id = self.kwargs.get('instructor_id')
        courses = self.get_queryset().filter(course_instructor__id=instructor_id)
        serializer = self.get_serializer(courses, many=True)
        return Response(serializer.data)


class CourseEnrollView(generics.CreateAPIView):
    serializer_class = CourseEnrollSerializer

    def create(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        user_id = self.kwargs.get('user_id')
        try:
            user = UserModel.objects.get(id=user_id)
            if user.is_instructor:
                return Response("Instructor cannot buy course")
        except UserModel.DoesNotExist:
            return Response("User not found", status=404)

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.validated_data['user'] = user
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)


class EnrolledCourseListOfStudent(generics.ListAPIView):
    queryset = CourseEnroll.objects.all()
    serializer_class = EnrolledCoursesSerializer

    def list(self, request, *args, **kwargs):
        user_id = self.kwargs.get('user_id')
        courses = self.get_queryset().filter(user=user_id)
        serializer = self.get_serializer(courses, many=True)
        return Response(serializer.data)


class StudentListOfEnrolledCourseView(generics.ListAPIView):
    queryset = CourseEnroll.objects.all()
    serializer_class = StudentListOfEnrolledCourseSerializer

    def get_queryset(self):
        course_id = self.kwargs.get('course_id')
        return CourseEnroll.objects.filter(course_id=course_id)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
