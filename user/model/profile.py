from django.db import models
from user.models import UserModel


class InstructorProfile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    first_name = models.CharField(blank=True, max_length=30)
    last_name = models.CharField(blank=True, max_length=30)
    experience = models.IntegerField(blank=True, default=0)
    subject = models.CharField(blank=True, max_length=30)

    def save(self, *args, **kwargs):
        self.pk = self.user.pk
        super(InstructorProfile, self).save(*args, **kwargs)
