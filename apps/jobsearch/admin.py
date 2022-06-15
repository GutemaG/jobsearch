from django.contrib import admin
from .models import Applicant,Job,Company,Application
# Register your models here.
admin.site.register([Applicant, Application,Job,Company])