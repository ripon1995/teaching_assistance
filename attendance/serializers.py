from rest_framework import serializers

from attendance.models import Attendance
from student.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name']


class StudentAttendanceListSerializer(serializers.ModelSerializer):
    student = StudentSerializer()

    class Meta:
        model = Attendance
        fields = '__all__'


class UploadAttendanceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
