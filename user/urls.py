from django.urls import path
from user.views import RegisterUserView, UserRetrieveUpdateView, InstructorProfileRetrieveUpdateView

urlpatterns = [
    path('user/', RegisterUserView.as_view()),
    path('user/<int:pk>/', UserRetrieveUpdateView.as_view()),
    path('instructor/profile/<int:pk>/', InstructorProfileRetrieveUpdateView.as_view()),
]
