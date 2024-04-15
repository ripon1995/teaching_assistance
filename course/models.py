from django.db import models
from user.models import UserModel


class Course(models.Model):
    course_instructor = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=20)
    course_title = models.CharField(max_length=50)
    course_fee = models.CharField(max_length=10)
    current_student = models.IntegerField(default=0)
    capacity = models.IntegerField(default=100)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)


class CourseEnroll(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)