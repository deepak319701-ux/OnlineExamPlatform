from django.db import models
from django.contrib.auth.models import User
from exams.models import Exam
from questions.models import Question


class StudentAnswer(models.Model):

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )

    selected_answer = models.CharField(
        max_length=1,
        choices=[
            ("A", "Option A"),
            ("B", "Option B"),
            ("C", "Option C"),
            ("D", "Option D"),
        ]
    )

    is_correct = models.BooleanField(default=False)

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.question.id}"


class Result(models.Model):

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE
    )

    score = models.IntegerField(default=0)

    total_marks = models.IntegerField(default=0)

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.student.username} - "
            f"{self.exam.title} ({self.score}/{self.total_marks})"
        )