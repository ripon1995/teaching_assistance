from django.urls import path
from course.views import CourseCreateView, CourseRetrieveUpdateView, CourseListView, CourseListViewOfSingleInstructor

urlpatterns = [
    path('course/', CourseCreateView.as_view()),
    path('course/<int:pk>/', CourseRetrieveUpdateView.as_view()),
    path('courses/', CourseListView.as_view()),
    path('courses/<int:instructor_id>/', CourseListViewOfSingleInstructor.as_view())
]
