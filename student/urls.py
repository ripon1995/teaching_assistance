from django.urls import path

from student.views import StudentCreateView, StudentRetrieveView, StudentAttendanceListView

urlpatterns = [
    path('student/', StudentCreateView.as_view()),
    path('student/<int:student_id>/<int:course_id>/', StudentRetrieveView.as_view()),
    path('course/<int:course_id>/student/attendance/', StudentAttendanceListView.as_view()),
]
