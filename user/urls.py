from django.urls import path
from user.views import RegisterUserView, UserRetrieveUpdateView, UserProfileRetrieveView

urlpatterns = [
    path('user/', RegisterUserView.as_view()),
    path('user/<int:pk>/', UserRetrieveUpdateView.as_view()),
    path('instructor/profile/<int:pk>/', UserProfileRetrieveView.as_view()),
]
