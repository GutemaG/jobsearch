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
        if self.company:
            return True
        return False
    
    def is_admin(self):
        return self.user_type=="ADMIN" and self.is_superuser