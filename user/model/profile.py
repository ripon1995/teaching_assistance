from django.db import models
from user.models import UserModel


class Profile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, primary_key=True)
    is_instructor = models.BooleanField(default=False)
    first_name = models.CharField(blank=True, max_length=30)
    last_name = models.CharField(blank=True, max_length=30)
