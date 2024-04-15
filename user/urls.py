from django.urls import path
from user.views import RegisterUserView, UserRetrieveUpdateView, UserProfileRetrieveView, ProfileUpdateView

urlpatterns = [
    path('user/', RegisterUserView.as_view()),
    path('user/<int:pk>/', UserRetrieveUpdateView.as_view()),
    path('profile/<int:pk>/', UserProfileRetrieveView.as_view()),
    path('profile/update/<int:pk>/', ProfileUpdateView.as_view())
]
