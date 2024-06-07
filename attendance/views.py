import datetime

from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from attendance.models import Attendance
from attendance.serializers import StudentAttendanceListSerializer, AttendancesUpdateSerializer, \
    AttendanceUpdateSerializer
from course.models import Course
from student.models import Student


class StudentAttendanceListView(generics.ListAPIView):
    serializer_class = StudentAttendanceListSerializer

    def get_queryset(self):
        course_id = self.kwargs.get('course_id')
        course = get_object_or_404(Course, pk=course_id)
        queryset = Student.objects.filter(course=course)
        today = datetime.date.today()
        attendance_records = []
        for student in queryset:
            attendance, created = Attendance.objects.get_or_create(student=student, course=course, date=today)
            attendance_records.append(attendance)
        return attendance_records


class UpdateStudentsAttendanceView(generics.UpdateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendancesUpdateSerializer

    def get_queryset(self):
        course_id = self.kwargs.get('course_id')
        course = get_object_or_404(Course, pk=course_id)
        queryset = Attendance.objects.filter(course=course)
        return queryset

    def update(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = request.data
        serializer = self.serializer_class(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        updated_instances = serializer.update(queryset, serializer.validated_data)
        updated_serializer = self.get_serializer(updated_instances, many=True)
        return Response(updated_serializer.data, status=status.HTTP_200_OK)


class UpdateStudentAttendanceView(generics.UpdateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceUpdateSerializer
