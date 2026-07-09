from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import StudentProfileForm
from .models import StudentProfile
from exams.models import Exam




def home(request):
    return render(request, 'home.html')


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
            password=password
        )

        messages.success(request, "Registration successful! Please login.")
        return redirect("register")

    return render(request, "register.html")
def user_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("dashboard")

        else:

            messages.error(request, "Invalid Username or Password")

    return render(request, "login.html")

#Dashborad section


@login_required
def dashboard(request):

    exams = Exam.objects.filter(is_active=True)

    return render(
        request,
        "dashboard.html",
        {
            "exams": exams
        }
    )

#student profile files

@login_required
def profile(request):

    try:
        profile = StudentProfile.objects.get(user=request.user)

    except StudentProfile.DoesNotExist:
        profile = StudentProfile(user=request.user)

    if request.method == "POST":

        form = StudentProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )
    

        if form.is_valid():

            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            messages.success(request, "Profile Updated Successfully")
            return redirect("dashboard")

        else:
            print(form.errors)

    else:
        form = StudentProfileForm(instance=profile)

    return render(request, "profile.html", {"form": form})
from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    return redirect("login")