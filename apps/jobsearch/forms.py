from dataclasses import field, fields
from django import forms
from django.forms import ModelForm
from apps.jobsearch.models import Application, Job
import datetime


class JobCreationForm(ModelForm):

    class Meta:
        model = Job
        # fields=["start_date","end_date","title","description",
        #         "category","requirement","education_level","experience",
        #         "experience_year","salary","type","region","vacancy"]
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Job Title"}),
            'education_level': forms.Select(
                attrs={"class": "form-control"}),
            'type': forms.Select(
                attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter Email address"}),
            'requirement': forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Job Requirement","rows":"3"}),
            'experience': forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Job Description","rows":"3"}),
            'experience_year': forms.NumberInput(
                attrs={"class": "form-control"}),
            'salary': forms.NumberInput(
                attrs={"class": "form-control"}),
            'vacancy': forms.NumberInput(
                attrs={"class": "form-control"}),
            'description': forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Job Description","rows":"3"}),
            'region': forms.Select(
                attrs={"class": "form-control"}),
            'company': forms.Select(
                attrs={"class": "form-control"}),
            'category': forms.Select(
                attrs={"class": "form-control"}),
            'start_date': forms.DateInput(attrs={
                "placeholder": "Start Application Date",
                "class": "form-control",
                'type': 'date',
            }),
            'end_date': forms.DateInput(attrs={
                "placeholder": "End Application Date",
                "class": "form-control",
                'type': 'date',
            }),

            # 'experience_year': forms.IntegerField(),
        }



class JobApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ["about_yourself","resume"]
        widgets={
            'resume': forms.FileInput(
                attrs={"class": "form-control",}),
            'about_yourself': forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Write about your self"}),
        }