from email.mime import application
from django.shortcuts import redirect, render
from django.db.models import Count

from django.contrib.auth.decorators import login_required
from apps.jobsearch.forms import JobApplicationForm, JobCreationForm
from .models import Application, Company, Job
from ..constants import JOB_CATEGORIES, JOB_TYPE_CHOICES, REGION_CHOICES
# Create your views here.
from .models import Job


def index(request):
    jobs = Job.objects.all()
    categories = jobs.values('category').annotate(
        total=Count('category')).order_by('-total')
    if request.GET.get('q'):
        print(request.GET.get('q'))
    context = {
        'categories': categories
    }
    return render(request, 'index.html', context=context)


def job_detail(request):
    return render(request, 'jobsearch/job_details.html')


def job_list(request, category=None):
    jobs = Job.objects.all()
    query = request.GET
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
        print(year)
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

    if category:
        jobs = Job.objects.filter(category=category)
    context = {
        'jobs': jobs,
        'job_category': JOB_CATEGORIES,
        'job_location': REGION_CHOICES,
        'job_type': JOB_TYPE_CHOICES
    }
    return render(request, 'jobsearch/job_listing.html', context=context)


def job_apply2(request, pk):
    job = Job.objects.get(pk=pk)
    application_form = JobApplicationForm()
    context = {
        'job': job,
        'form': application_form
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
        return redirect('job-detail', pk)
    return render(request, 'jobsearch/job_apply.html', context=context)


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


def job_post2(request):
    job_form = JobCreationForm
    if request.method == 'POST':
        job_title = request.POST.get('job-title')
        job_description = request.POST.get('job-description')
        job_requirement = request.POST.get('job-requirement')
        job_experience = request.POST.get('job-experience')
        job_start_date = request.POST.get('job-start_date')
        job_end_date = request.POST.get('job-end_date')
        job_salary = request.POST.get('job-salary')
        job_category = request.POST.get('job-category')
        job_educational_level = request.POST.get('job-educational_level')
        job_type = request.POST.get('job-type')
        job_location = request.POST.get('job-location')
        job_company = request.POST.get('job-company')
        job_experience_year = request.POST.get('job-experience_year')

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
    context = {'job_form': job_form}
    return render(request, 'jobsearch/job_post.html', context=context)


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
            # print("invalid")
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
