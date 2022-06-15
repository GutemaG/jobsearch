from operator import mod
from statistics import mode
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

from .constants import (JOB_CATEGORIES,
    CITY_CHOICE,
    EDUCATIONAL_LEVEL_CHOICES,
    GENDER_CHOICES,
    REGION_CHOICES,
    JOB_TYPE_CHOICES,
    APPLICATION_STATUS_CHOICES
    )

class Applicant(models.Model):
    # primary attributes: username,password,email,first_name,last_name
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=2,choices=GENDER_CHOICES)
    phone = models.CharField(max_length=13)
    region = models.CharField(max_length=30,choices=REGION_CHOICES)
    city = models.CharField(max_length=15,choices=CITY_CHOICE)
    education_level = models.CharField(max_length=15,choices=EDUCATIONAL_LEVEL_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resume = models.FileField(upload_to='./cv',blank=True,null=True)

    def __str__(self):
        return self.user.username


class Company(models.Model):
    employee = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    region = models.CharField(max_length=30,choices=REGION_CHOICES)
    city = models.CharField(max_length=15,choices=CITY_CHOICE)
    # document = models.FileField(upload_to="company",blank=True,null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# TODO: add email address, status(approved || not), file appload
    def __str__(self):
        return self.name

class Job(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=300)
    description = models.TextField()
    category = models.CharField(max_length=40,choices=JOB_CATEGORIES)
    requirement = models.TextField(help_text='requirements for job')
    education_level = models.CharField(max_length=15,choices=EDUCATIONAL_LEVEL_CHOICES)
    experience = models.TextField(help_text='required experience for job')
    experience_year = models.IntegerField(default=0)
    salary = models.IntegerField(default=0)

    type = models.CharField(max_length=15,choices=JOB_TYPE_CHOICES)
    region = models.CharField(max_length=30,choices=REGION_CHOICES)
    
    # TODO: location - region and add city, add vacancy(how many person required)
    # city
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Application(models.Model):
    # Todo: change user to applicant
    user = models.ForeignKey(Applicant,on_delete=models.CASCADE)
    job = models.ForeignKey(Job,on_delete=models.DO_NOTHING)
    resume = models.FileField(upload_to='./cv',blank=True,null=True)
# todo: about your self
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # status = models.CharField(max_length=20, choices=APPLICATION_STATUS_CHOICES,default="PENDING")

    def __str__(self):
        return self.job.title

# TODO: Actors: Applicant, Admin, Employer,
"""
post job
apply job
register(applicant, employee)
login
create company
approve company

"""