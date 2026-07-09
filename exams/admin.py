from django.contrib import admin
from .models import Exam

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "subject",
        "duration",
        "total_marks",
        "passing_marks",
        "is_active",
    )

    list_filter = ("subject", "is_active")

    search_fields = ("title", "subject")