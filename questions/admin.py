from django.contrib import admin
from .models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):

    list_display = (
        "question",
        "exam",
        "correct_answer",
        "marks",
    )

    list_filter = (
        "exam",
    )

    search_fields = (
        "question",
    )