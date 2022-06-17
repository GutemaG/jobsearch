from ast import Mod
from dataclasses import fields
import email
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from apps import user

from apps.constants import CITY_CHOICE, EDUCATIONAL_LEVEL_CHOICES, GENDER_CHOICES, REGION_CHOICES, USER_TYPE_CHOICE
from .models import User
from apps.jobsearch.models import Applicant, Company
from django.contrib.auth.forms import AuthenticationForm

user_creation_widgets = {
            'first_name': forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter First Name","required":""}),
            'last_name': forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Last Name","required":""}),
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
            'email':forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter Email address"}),
        }

class UserRegisetrationForm(UserCreationForm):
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
                  "last_name", "gender", "phone", "region", "city", "user_type","email"}
        # exclude = []
        widgets = user_creation_widgets

class LoginForm(AuthenticationForm):
    class Meta:
        widgets={
        'username': forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Username"}),
         'password1': forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Password",'type':'password'}),
            
        }


class ProfileUpdateForm(ModelForm):
    class Meta:
        model=User
        fields = {"username", "first_name",
                  "last_name", "gender", "phone", "region", "city", "user_type","email"}
        widgets = user_creation_widgets

class ApplicantCreationForm(ModelForm):
    class Meta:
        model = Applicant
        fields = {"education_level", "resume"}
        widgets = {
            'education_level': forms.Select(
                attrs={"class": "form-control", 
                }),
            'resume': forms.FileInput(
                attrs={"class": "form-control", 
                }),
          
        }

class CompanyUpdateForm(ModelForm):

    class Meta:
        model = Company
        fields = ["name","region","email","city","document","description"]
        widgets={
            'name': forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Company Name"}),
            'region': forms.Select(choices=REGION_CHOICES,
                                   attrs={"class": "form-control"}),
            'city': forms.Select(
                                 attrs={"class": "form-control"}),
            'email':forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter Email address"}),
            'document': forms.FileInput(
                attrs={"class": "form-control", 
                }),
            'description': forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Company Description"}),
        }