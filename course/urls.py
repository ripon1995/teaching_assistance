from django.urls import path
from course.views import CourseCreateView, CourseRetrieveUpdateView, CourseListView

urlpatterns = [
    path('course/', CourseCreateView.as_view()),
    path('course/<int:pk>/', CourseRetrieveUpdateView.as_view()),
    path('courses/', CourseListView.as_view()),
]
