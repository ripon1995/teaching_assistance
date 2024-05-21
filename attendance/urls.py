from django.urls import path

from attendance.views import StudentAttendanceListView, UploadStudentAttendanceView

urlpatterns = [
    path('attendance/<int:course_id>/', StudentAttendanceListView.as_view()),
    path('attendance/', UploadStudentAttendanceView.as_view())
]
