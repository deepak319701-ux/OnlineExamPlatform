from django import forms
from .models import StudentProfile


class StudentProfileForm(forms.ModelForm):

    class Meta:
        model = StudentProfile

        fields = [
            "full_name",
            "roll_number",
            "branch",
            "year",
            "mobile",
            "college",
            "profile_picture",
        ]

        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control"}),
            "roll_number": forms.TextInput(attrs={"class": "form-control"}),
            "branch": forms.TextInput(attrs={"class": "form-control"}),
            "year": forms.TextInput(attrs={"class": "form-control"}),
            "mobile": forms.TextInput(attrs={"class": "form-control"}),
            "college": forms.TextInput(attrs={"class": "form-control"}),
        }