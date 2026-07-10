from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from exams.models import Exam
from .models import StudentAnswer, Result
from django.http import HttpResponse
from .certificate import generate_certificate


@login_required
def my_results(request):
    

    results = Result.objects.filter(
        student=request.user
    ).order_by("-submitted_at")

    return render(
        request,
        "results/my_results.html",
        {
            "results": results
        }
    )
@login_required
def download_certificate(request, exam_id):

    exam = get_object_or_404(Exam, id=exam_id)

    result = get_object_or_404(
        Result,
        student=request.user,
        exam=exam
    )

    # Certificate sirf PASS students download kar sakte hain

    
    if result.score < exam.passing_marks:
        return HttpResponse(
            "Certificate is available only for passed students."
        )

    percentage = round(
        (result.score / result.total_marks) * 100,
        2
    )

    response = HttpResponse(content_type="application/pdf")

    response["Content-Disposition"] = (
        f'attachment; filename="{exam.title}_certificate.pdf"'
    )

    generate_certificate(
        response,
        request.user.username,
        exam.title,
        result.score,
        percentage
    )

    return response
@login_required
def leaderboard(request):

    leaderboard = Result.objects.select_related(
        "student",
        "exam"
    ).order_by("-score")

    return render(
        request,
        "results/leaderboard.html",
        {
            "leaderboard": leaderboard
        }
    )
def result_page(request, exam_id):

    exam = get_object_or_404(Exam, id=exam_id)

    answers = StudentAnswer.objects.filter(
        student=request.user,
        exam=exam
    )

    total_questions = exam.questions.count()

    correct_answers = answers.filter(is_correct=True).count()

    wrong_answers = total_questions - correct_answers

    score = 0

    for answer in answers:
        if answer.is_correct:
            score += answer.question.marks

    total_marks = sum(
        question.marks for question in exam.questions.all()
    )

    Result.objects.update_or_create(
        student=request.user,
        exam=exam,
        defaults={
            "score": score,
            "total_marks": total_marks
        }
    )

    percentage = 0

    if total_marks > 0:
        percentage = round((score / total_marks) * 100, 2)

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