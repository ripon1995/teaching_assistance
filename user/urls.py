from django.urls import path
from user.views import RegisterUserView

urlpatterns = [
    path('user/', RegisterUserView.as_view())
]
