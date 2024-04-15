from django.urls import path

from student.views import StudentCreateView

urlpatterns = [
    path('student/<int:course_id>/add/', StudentCreateView.as_view())
]