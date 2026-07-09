from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from exams.models import Exam
from .models import StudentAnswer, Result


@login_required
def result_page(request, exam_id):

    exam = get_object_or_404(Exam, id=exam_id)

    answers = StudentAnswer.objects.filter(
        student=request.user,
        exam=exam
    )

    total_questions = answers.count()

    correct_answers = answers.filter(
        is_correct=True
    ).count()

    wrong_answers = total_questions - correct_answers

    score = 0

    for answer in answers:

        if answer.is_correct:
            score += answer.question.marks

    total_marks = sum(
        question.marks
        for question in exam.questions.all()
    )

    Result.objects.update_or_create(

        student=request.user,

        exam=exam,

        defaults={
            "score": score,
            "total_marks": total_marks,
        }
    )

    percentage = 0

    if total_marks > 0:
        percentage = (score / total_marks) * 100

    status = "PASS"

    if score < exam.passing_marks:
        status = "FAIL"

    return render(
        request,
        "results/result.html",
        {
            "exam": exam,
            "score": score,
            "total_marks": total_marks,
            "correct_answers": correct_answers,
            "wrong_answers": wrong_answers,
            "percentage": percentage,
            "status": status,
        }
    )