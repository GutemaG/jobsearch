from turtle import title
from unicodedata import category
from django.shortcuts import redirect, render
from django.db.models import Count
from .models import Application, Company, Job
# Create your views here.
from .models import Job
def index(request):
    jobs = Job.objects.all()
    categories = jobs.values('category').annotate(total=Count('category')).order_by('-total')
    context = {
        'categories':categories
    }
    return render(request, 'jobsearch/index.html',context=context)
def job_detail(request):
    return render(request, 'jobsearch/job_details.html')

def job_list(request):
    jobs = Job.objects.all()
    context = {
        'jobs':jobs
    }
    print(jobs)
    return render(request, 'jobsearch/job_listing.html',context=context)
    
def job_apply(request,pk):
    job = Job.objects.get(pk=pk)
    context = {
        'job':job
    }
    if request.method == "POST":
        user = request.user.applicant
        if(request.FILES['resume']):
            print(request.FILES['resume'])
        else:
            print("empty")
        # Application.objects.create(
        #     user=user,
        #     job=job,
        #     resume=resume
        # )
        return redirect('job-detail',pk)
    return render (request, 'jobsearch/job_apply.html',context=context)

def job_post(request):
    if request.method=='POST':
        job_title = request.POST.get('job-title')
        job_description =  request.POST.get('job-description')
        job_requirement = request.POST.get('job-requirement')
        job_experience =  request.POST.get('job-experience')
        job_start_date =  request.POST.get('job-start_date')
        job_end_date =  request.POST.get('job-end_date')
        job_salary =  request.POST.get('job-salary')
        job_category =  request.POST.get('job-category')
        job_educational_level =  request.POST.get('job-educational_level')
        job_type =  request.POST.get('job-type')
        job_location =  request.POST.get('job-location')
        job_company =  request.POST.get('job-company')
        job_experience_year=request.POST.get('job-experience_year')

        c = Company.objects.first()
        job = Job.objects.create(
            title=job_title,
            start_date=job_start_date,
            end_date=job_end_date,
            description=job_description,
            category=job_category,
            requirement=job_requirement,
            education_level=job_educational_level,
            experience=job_experience,
            experience_year=job_experience_year,
            salary=job_salary,
            type=job_type,
            region=job_location,
            company=c
        )
    return render (request, 'jobsearch/job_post.html')

def job_detail(request, pk):
    job = Job.objects.get(pk=pk)
    context = {
        'job':job
    }
    return render(request, 'jobsearch/job_details.html',context=context)

    """company
start_date 
end_date
title
description 
category 
requirement 
education_level 
experience 
experience_year 
salary 
type 
location"""

def job_application_list(request):
    applications = Application.objects.all()
    context = {
        'applications':applications
    }
    return render(request,'jobsearch/job_application_list.html',context=context)

def job_application_detail(request,pk):
    application = Application.objects.get(pk=pk)
    context = {
        'application':application
    }
    return render(request,'jobsearch/job_application_detail.html',context=context)
"""
 # print(request.POST.get('job_title'))
        print("job_title", job_title)
        print("job_description ",job_description)
        print("job_description", job_description)
        print("job_requirement", job_requirement)
        print("job_experience", job_experience)
        print("job_start_date", job_start_date)
        print("job_end_date", job_end_date)
        print("job_salary", job_salary)
        print("job_category", job_category)
        print("job_educational_level ",job_educational_level)
        print("job_type ",job_type)
        print("job_location ",job_location)
        print("job_company ",job_company)
        print("job_experience_year ",job_experience_year)
"""