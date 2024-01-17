from django.db import models


# Create your models here.
class UserModel(models.Model):
    user_name = models.CharField(unique=True, max_length=30)
    is_instructor = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    password = models.CharField(blank=False, max_length=30)
