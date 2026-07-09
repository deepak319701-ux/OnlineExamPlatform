from django.shortcuts import render, get_object_or_404, redirect
from exams.models import Exam
from .models import Question
from results.models import StudentAnswer
from django.contrib.auth.decorators import login_required


@login_required
def exam_page(request, exam_id):

    exam = get_object_or_404(Exam, id=exam_id)

    questions = exam.questions.all()

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
        },
    )