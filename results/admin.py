from django.contrib import admin
from .models import StudentAnswer, Result


@admin.register(StudentAnswer)
class StudentAnswerAdmin(admin.ModelAdmin):

    list_display = (
        "student",
        "exam",
        "question",
        "selected_answer",
        "is_correct",
    )


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):

    list_display = (
        "student",
        "exam",
        "score",
        "total_marks",
    )