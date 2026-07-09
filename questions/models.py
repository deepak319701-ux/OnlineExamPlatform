from django.db import models
from exams.models import Exam


class Question(models.Model):

    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE,
        related_name="questions"
    )

    question = models.TextField()

    option_a = models.CharField(max_length=255)

    option_b = models.CharField(max_length=255)

    option_c = models.CharField(max_length=255)

    option_d = models.CharField(max_length=255)

    ANSWERS = [
        ("A", "Option A"),
        ("B", "Option B"),
        ("C", "Option C"),
        ("D", "Option D"),
    ]

    correct_answer = models.CharField(
        max_length=1,
        choices=ANSWERS
    )

    marks = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.question[:50]