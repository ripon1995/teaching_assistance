from django.db import models

from course.models import Course


class Student(models.Model):
    name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)
    mother_name = models.CharField(max_length=30)
    institution = models.CharField(max_length=30)
    contact_number = models.CharField(max_length=30)
    father_contact_number = models.CharField(max_length=30)
    start_date = models.DateField(auto_now=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
