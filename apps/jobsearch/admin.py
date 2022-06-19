from django.contrib import admin
from .models import Job,Company,Application
# Register your models here.
admin.site.register([Application,Job,Company])