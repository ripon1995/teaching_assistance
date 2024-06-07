from django.urls import path

from attendance.views import StudentAttendanceListView, UpdateStudentsAttendanceView, UpdateStudentAttendanceView

urlpatterns = [
    path('attendance/<int:course_id>/', StudentAttendanceListView.as_view()),
    path('attendance/<int:course_id>/update/', UpdateStudentsAttendanceView.as_view()),
    path('attendance/update/<int:pk>/', UpdateStudentAttendanceView.as_view())
]
