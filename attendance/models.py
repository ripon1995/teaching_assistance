from django.db import models

from course.models import Course
from student.models import Student


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.BooleanField(default=True)

    # class Meta:
    #     unique_together = ('student', 'course', 'date')
