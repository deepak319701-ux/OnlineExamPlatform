from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from exams.models import Exam
from .models import Question
from results.models import StudentAnswer, Result


@login_required
def exam_page(request, exam_id):

    # Get Exam
    exam = get_object_or_404(Exam, id=exam_id)

    # Prevent multiple attempts
    if Result.objects.filter(
        student=request.user,
        exam=exam
    ).exists():

        messages.warning(
            request,
            "You have already attempted this exam."
        )

        return redirect("dashboard")

    # Get Questions
    questions = exam.questions.all()

    # Submit Exam
    if request.method == "POST":

        for question in questions:

            selected = request.POST.get(
                f"question_{question.id}"
            )

            if selected:

                StudentAnswer.objects.create(
                    student=request.user,
                    exam=exam,
                    question=question,
                    selected_answer=selected,
                    is_correct=(selected == question.correct_answer),
                )

        return redirect("result_page", exam_id=exam.id)

    return render(
        request,
        "questions/exam_page.html",
        {
            "exam": exam,
            "questions": questions,
        }
    )