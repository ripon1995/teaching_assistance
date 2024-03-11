from rest_framework import serializers
from course.models import Course, CourseEnroll


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseEnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseEnroll
        fields = ['course']


class EnrolledCoursesSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source='course.course_title')

    class Meta:
        model = CourseEnroll
        fields = ['course_title']


class StudentListOfEnrolledCourseSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='user.user_name')

    class Meta:
        model = CourseEnroll
        fields = ['student_name']
