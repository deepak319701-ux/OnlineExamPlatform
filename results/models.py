from django.db import models
from django.contrib.auth.models import User
from exams.models import Exam
from questions.models import Question
from datetime import datetime


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


    def save(self, *args, **kwargs):

        if not self.certificate_number:

            year = datetime.now().year

            last_result = Result.objects.order_by("-id").first()

            if (
                last_result
                and last_result.certificate_number
                and "-" in last_result.certificate_number
            ):
                try:
                    last_number = int(
                        last_result.certificate_number.split("-")[-1]
                    )
                except ValueError:
                    last_number = 0
            else:
                last_number = 0

            

        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"{self.student.username} - "
            f"{self.exam.title} ({self.score}/{self.total_marks})"
        )