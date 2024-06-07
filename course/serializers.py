from rest_framework import serializers
from course.models import Course, CourseEnroll
from user.models import UserModel


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'user_name']


class CourseSerializer(serializers.ModelSerializer):
    course_instructor = InstructorSerializer(read_only=True)

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
