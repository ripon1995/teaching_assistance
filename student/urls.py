from django.urls import path

from student.views import StudentCreateView, StudentRetrieveView, StudentUpdateView

urlpatterns = [
    path('student/', StudentCreateView.as_view()),
    path('student/<int:pk>/update/', StudentUpdateView.as_view()),
    path('student/<int:pk>/<int:course_id>/', StudentRetrieveView.as_view()),
]
