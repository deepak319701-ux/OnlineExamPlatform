from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from exams.models import Exam
from results.models import Result

from .forms import StudentProfileForm
from .models import StudentProfile



#==================
#.  for admin login
#=============

from django.contrib.auth.models import User
from django.http import HttpResponse

# ==========================
# Home
# ==========================

def home(request):
    return render(request, "home.html")


# ==========================
# Register
# ==========================

def register(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect("register")

        User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )

        messages.success(
            request,
            "Registration Successful! Please Login."
        )

        return redirect("login")

    return render(request, "register.html")


# ==========================
# Login
# ==========================

def user_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is not None:

            login(request, user)

            return redirect("dashboard")

        else:

            messages.error(
                request,
                "Invalid Username or Password"
            )

    return render(request, "login.html")


# ==========================
# Dashboard
# ==========================

@login_required
def dashboard(request):

    exams = Exam.objects.all()

    results = Result.objects.filter(
        student=request.user
    )

    attempted = list(
        results.values_list(
            "exam_id",
            flat=True
        )
    )

    total_exams = exams.count()

    attempted_count = results.count()

    remaining_count = total_exams - attempted_count

    certificate_count = results.count()

    context = {

        "exams": exams,

        "attempted": attempted,

        "total_exams": total_exams,

        "attempted_count": attempted_count,

        "remaining_count": remaining_count,

        "certificate_count": certificate_count,

    }

    return render(
        request,
        "dashboard.html",
        context,
    )


# ==========================
# Logout
# ==========================

def user_logout(request):

    logout(request)

    messages.success(
        request,
        "Logged out successfully."
    )

    return redirect("login")


# ==========================
# Student Profile
# ==========================

@login_required
def profile(request):

    profile, created = StudentProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":

        form = StudentProfileForm(
            request.POST,
            request.FILES,
            instance=profile,
        )

        if form.is_valid():

            profile = form.save(
                commit=False
            )

            profile.user = request.user

            profile.save()

            messages.success(
                request,
                "Profile Updated Successfully."
            )

            return redirect("profile")

    else:

        form = StudentProfileForm(
            instance=profile
        )

    return render(
        request,
        "profile.html",
        {
            "form": form
        }
    )
#==================
#.  for admin login
#=============
    def create_admin(request):

     username = "admin"

    password = "Admin@952336"

    email = "admin@example.com"

    if User.objects.filter(username=username).exists():
        return HttpResponse("Admin already exists.")

    User.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )

    return HttpResponse("Admin created successfully.")