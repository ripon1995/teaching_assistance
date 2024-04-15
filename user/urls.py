from django.urls import path
from user.views import RegisterUserView, UserRetrieveUpdateView

urlpatterns = [
    path('user/', RegisterUserView.as_view()),
    path('user/<int:pk>/', UserRetrieveUpdateView.as_view()),
]
