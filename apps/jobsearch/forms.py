from dataclasses import field
from django import forms
from django.forms import ModelForm
from apps.jobsearch.models import Job


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
            'requirement': forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Job Requirement"}),
            'experience': forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Job Description"}),
            'description': forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Job Description"}),
            'region': forms.Select(
                attrs={"class": "form-control"}),
            'company': forms.Select(
                attrs={"class": "form-control"}),
            'category': forms.Select(
                attrs={"class": "form-control"}),
            
            # 'experience_year': forms.IntegerField(),
        }
