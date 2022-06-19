from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from ..constants import (JOB_CATEGORIES,
    CITY_CHOICE,
    EDUCATIONAL_LEVEL_CHOICES,
    GENDER_CHOICES,
    REGION_CHOICES, USER_TYPE_CHOICE,
    )

class User(AbstractUser):
    gender = models.CharField(max_length=2,choices=GENDER_CHOICES)
    phone = models.CharField(max_length=20)
    region = models.CharField(max_length=30,choices=REGION_CHOICES)
    city = models.CharField(max_length=15,choices=CITY_CHOICE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_type = models.CharField(max_length=20,choices=USER_TYPE_CHOICE,default="APPLICANT")

    def have_company(self):
        if self.employer.company:
            return True
        return False
    
    def is_admin(self):
        return self.user_type=="ADMIN" and self.is_superuser
    def is_employer(self):
        return self.user_type == "EMPLOYEE"
    
    def can_register_company(self):
        return self.employer
    
    def is_company_employer_is_approved(self):
        return self.employer and self.employer.approved and self.employer.company.status

class Applicant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    education_level = models.CharField(max_length=15,choices=EDUCATIONAL_LEVEL_CHOICES)
    resume = models.FileField(upload_to='./cv',blank=True,null=True)
    def __str__(self):
        return self.user.username

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username