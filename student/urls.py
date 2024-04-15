from django.urls import path

from student.views import StudentCreateView, StudentRetrieveView

urlpatterns = [
    path('course/<int:course_id>/student/', StudentCreateView.as_view()),
    path('course/<int:course_id>/student/<int:student_id>/', StudentRetrieveView.as_view())
]
