from django.contrib import admin
from .models import Employer, User,Applicant

# Register your models here.
admin.site.register([User,Applicant,Employer])