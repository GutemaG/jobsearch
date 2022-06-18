from email.mime import application
from multiprocessing import context
from unicodedata import category
from django.shortcuts import redirect, render
from django.db.models import Count
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from pkg_resources import Requirement
from apps.jobsearch.forms import JobApplicationForm, JobCreationForm
from .models import Application, Company, Job
from ..constants import JOB_CATEGORIES, JOB_TYPE_CHOICES, REGION_CHOICES
from .models import Job
from django.db.models import Q
# Create your views here.
def index(request):
    jobs = Job.objects.all()
    categories = jobs.values('category').annotate(
        total=Count('category')).order_by('-total')
    if request.GET.get('q'):
        print(request.GET.get('q'))
    recent_jobs = jobs.order_by('-created_at')[:3]
    context = {
        'categories': categories,
        'recent_jobs':recent_jobs
    }

    return render(request, 'index.html', context=context)

def job_list(request, category=None):
    jobs = Job.objects.all()
    query = request.GET
    # category_from_index
    if request.GET.get('category_from_index'):
        jobs = jobs.filter(category=request.GET.get('category_from_index'))
    if(query.get('category')):
        cat = query.get('category')
        if cat != "all":
            jobs = jobs.filter(category=cat)
        if query.get('job_type'):
            job_type = request.GET.getlist('job_type')
            jobs = jobs.filter(type__in=job_type)
        loc = query.get('location')
        if loc != "anywhere":
            jobs = jobs.filter(region=loc)
        min_salary = query.get('min-salary')
        max_salary = query.get('max-salary')
        if(min_salary):
            # gte==greater than or equal to, >=
            jobs = jobs.filter(salary__gte=min_salary)
        if(max_salary):
            # gte==less than or equal to, <=
            jobs = jobs.filter(salary__lte=max_salary)
        year = query.get('experience_year')
        if year:
            if year == ">6":
                jobs = jobs.filter(experience_year__gte=6)
            else:
                minYear = year[0]
                maxYear = year[2]
                jobs = jobs.filter(experience_year__gte=minYear)
                jobs = jobs.filter(experience_year__lte=maxYear)
        
        posted_in = query.get('posted_in')
        if posted_in:
            from django.utils import timezone
            today = timezone.now().date().day
            if posted_in != "today" and posted_in != "any":
                jobs = jobs.filter(created_at__day__lte=today-int(posted_in))
            if posted_in == "today":
                jobs = jobs.filter(created_at__day=today)


    if request.GET.get('jobSort'):
        sort = request.GET.get('jobSort')
        if sort=="TIME":
            jobs = jobs.order_by('-created_at')
        elif sort=="Year_Dsc":
            print("Dec")
            jobs = jobs.order_by('-experience_year')
        elif sort=="Year_Asc":
            jobs = jobs.order_by('experience_year')
        elif sort=="Salary_Desc":
            jobs = jobs.order_by('salary')
        
        elif sort=="Salary_Asc":
            jobs = jobs.order_by('-salary')
    
    paginator = Paginator(jobs,5)
    page_number = request.GET.get('page')
    jobs = paginator.get_page(page_number)
    context = {
        'jobs': jobs,
        'job_category': JOB_CATEGORIES,
        'job_location': REGION_CHOICES,
        'job_type': JOB_TYPE_CHOICES,
    }
    return render(request, 'jobsearch/job_listing.html', context=context)

@login_required
def job_apply(request, pk):
    job = Job.objects.get(pk=pk)
    application_form = JobApplicationForm()
    context = {
        'job': job,
        'form': application_form
    }
    if request.method == "POST":
        # user = request.user.applicant
        application_form = JobApplicationForm(request.POST, request.FILES)
        if application_form.is_valid():
            data = application_form.cleaned_data
            Application.objects.create(
                user=request.user.applicant,
                job=job,
                about_yourself=data['about_yourself'],
                resume=data['resume']
            )
            # print(application_form.cleaned_data)
        else:
            print("invalid")
    return render(request, 'jobsearch/job_apply.html', context=context)

@login_required
def job_post(request):
    job_form = JobCreationForm()
    if request.method == "POST":
        job_form = JobCreationForm(request.POST)
        if job_form.is_valid():
            job = job_form.save()
            return redirect('job-detail', job.pk)
        else:
            print(job_form.errors)
    context = {'job_form': job_form}
    return render(request, 'jobsearch/job_post.html', context=context)


def job_detail(request, pk):
    job = Job.objects.get(pk=pk)
    context = {
        'job': job
    }
    return render(request, 'jobsearch/job_details.html', context=context)

@login_required
def job_application_list(request):
    applications = Application.objects.all()
    context = {
        'applications': applications
    }
    return render(request, 'jobsearch/job_application_list.html', context=context)


@login_required
def job_user_application_list(request):
    user = request.user
    user_applications = user.applicant.application_set.all()
    context = {'applications': user_applications}
    return render(request, 'jobsearch/job_application_list.html', context=context)


@login_required
def job_application_detail(request, pk):
    application = Application.objects.get(pk=pk)
    context = {
        'application': application
    }
    return render(request, 'jobsearch/job_application_detail.html', context=context)


@login_required
def edit_job(request, pk):
    job = Job.objects.get(pk=pk)
    if request.method == "POST":
        j = JobCreationForm(request.POST, instance=job)
        if j.is_valid():
            j.save()
            return redirect('company-job-list')
        else:
            print("errors ", j.errors)
    context = {'job': job, 'job_form': JobCreationForm(instance=job)}
    return render(request, "jobsearch/edit_job.html", context=context)

def job_search(request):
    query = request.GET.get('search-query')
    context={}
    if(query):
        # jobs = None
        jobs = Job.objects.filter(
            Q(title__icontains=query) | Q(type__icontains=query) | 
            Q(category__icontains=query) | Q(requirement__icontains=query)|
            Q(region__icontains=query) | Q(description__icontains=query)
        )
        companies = Company.objects.filter(
            Q(name__icontains=query) | Q(region__icontains=query) | 
            Q(city__icontains=query) | Q(description__icontains=query)
        )
        context['jobs'] = jobs
        context['companies'] = companies
        return render(request,'jobsearch/search.html',context=context)
    else:
        return redirect('homer')