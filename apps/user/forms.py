from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm

from apps.constants import CITY_CHOICE, EDUCATIONAL_LEVEL_CHOICES, GENDER_CHOICES, REGION_CHOICES, USER_TYPE_CHOICE
from .models import User
from apps.jobsearch.models import Applicant


class UserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Confirm Password"})
    )

    class Meta:
        model = User
        fields = {"username", "password1", "password2", "first_name",
                  "last_name", "gender", "phone", "region", "city", "user_type"}
        # exclude = []
        widgets = {
            'first_name': forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter First Name"}),
            'last_name': forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Last Name"}),
            'phone': forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Phone Number"}),
            'username': forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Username"}),
            'gender': forms.Select(choices=GENDER_CHOICES,
                                   attrs={"class": "form-control"}),
            'region': forms.Select(choices=REGION_CHOICES,
                                   attrs={"class": "form-control"}),
            'city': forms.Select(
                                 attrs={"class": "form-control"}),
            'user_type': forms.Select(choices=[("APPLICANT","APPLICANT"),("EMPLOYEE","EMPLOYEE")],
                                 attrs={"class": "form-control"}),
        }


class ApplicantCreationForm(ModelForm):
    education_level = forms.CharField(
        widget=forms.Select(choices=EDUCATIONAL_LEVEL_CHOICES,
                            attrs={"class": "form-control", "placeholder": "Password"})
    )
    resume = forms.CharField(
        widget=forms.FileInput(
            attrs={"class": "form-control-file"})
    )

    class Meta:
        model = Applicant
        fields = {"education_level", "resume"}
