from django.db import models

class Exam(models.Model):

    title = models.CharField(max_length=200)

    subject = models.CharField(max_length=100)

    description = models.TextField(blank=True)

    duration = models.PositiveIntegerField(help_text="Duration in Minutes")

    total_marks = models.PositiveIntegerField()

    passing_marks = models.PositiveIntegerField()

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title