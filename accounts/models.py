from django.db import models
from django.contrib.auth.models import User


class StudentProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    full_name = models.CharField(max_length=100)

    roll_number = models.CharField(max_length=30)

    branch = models.CharField(max_length=50)

    year = models.CharField(max_length=20)

    mobile = models.CharField(max_length=15)

    college = models.CharField(max_length=200)

    profile_picture = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.full_name