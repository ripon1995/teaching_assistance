from django.urls import path
from course.views import CourseCreateView, CourseRetrieveUpdateView

urlpatterns = [
    path('course/', CourseCreateView.as_view()),
    path('course/<int:pk>/', CourseRetrieveUpdateView.as_view()),
]
