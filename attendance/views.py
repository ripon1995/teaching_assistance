import datetime

from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response

from attendance.models import Attendance
from attendance.serializers import StudentAttendanceListSerializer, UploadAttendanceListSerializer
from course.models import Course
from student.models import Student


class StudentAttendanceListView(generics.ListAPIView):
    serializer_class = StudentAttendanceListSerializer

    def get_queryset(self):
        course_id = self.kwargs.get('course_id')
        course = get_object_or_404(Course, pk=course_id)
        queryset = Student.objects.filter(course=course)
        next_day = datetime.date.today()
        attendance_records = []
        for student in queryset:
            attendance, created = Attendance.objects.get_or_create(student=student, course=course, date=next_day,
                                                                   defaults={'status': 'Present'})
            attendance_records.append(attendance)
        return attendance_records

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UploadStudentAttendanceView(generics.CreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = UploadAttendanceListSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
