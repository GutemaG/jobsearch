
from django.shortcuts import redirect, render
from apps.jobsearch.forms import JobApplicationForm, JobCreationForm
from apps.jobsearch.models import Application, Company, Job
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ApplicantCreationForm, CompanyUpdateForm, LoginForm, ProfileUpdateForm, UserRegisetrationForm

from .models import User
# Create your views here.

def login_user(request):
    u = LoginForm(request, data=request.POST)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            next = request.POST.get('next')
            if(next):
                return redirect(next)
            return redirect ('home')
        else:
            messages.warning(request,'Username or Password incorrect')
    context = {'login_form':u}
    return render (request, 'user/login.html',context=context)

def logout_user(request):
    logout(request)
    return render (request, 'user/login.html')

def register(request):
    profile_form = UserRegisetrationForm()
    applicant_form = ApplicantCreationForm()
    if request.method == "POST":
        profile_form = UserRegisetrationForm(data=request.POST)
        applicant_form = ApplicantCreationForm(request.POST,request.FILES)
        if profile_form.is_valid() and applicant_form.is_valid():
            user = profile_form.save()
            applicant = applicant_form.save(commit=False)
            applicant.user = user
            applicant.save()
            u = authenticate(request, username=request.POST['username'],password=request.POST['password1'])
            login(request,u)
            messages.success(request, "You Successfully Registered!")
            return redirect ('home')
        else:
            messages.warning(request, "Check your Form")
    
    context = {'form':profile_form,'applicant_form':applicant_form}
    return render (request, 'user/registration.html',context=context)


@login_required
def update_profile(request):
    user = request.user
    profile_form = ProfileUpdateForm(instance=user)
    applicant_form = ApplicantCreationForm(instance=user.applicant)
    if request.method=="POST":
        profile_form = ProfileUpdateForm(request.POST,instance=user)
        applicant_form = ApplicantCreationForm(request.POST,request.FILES,instance=user.applicant)
        if profile_form.is_valid() and applicant_form.is_valid():
            profile_form.save()
            applicant_form.save()
        else:
            messages.warning(request, "Check your Form!")

    context = {'form':profile_form,'applicant_form':applicant_form}
    return render (request, 'user/profile.html',context=context)


@login_required
def view_company(request):
    user = request.user
    user_company = user.company
    context={'company':user_company}
    return render(request, "user/company.html",context=context)

@login_required
def edit_company(request):
    user = request.user
    if request.method == "POST":
        c = CompanyUpdateForm(request.POST,request.FILES,instance=user.company)
        if c.is_valid():
            c.save()
            return redirect('your-company')
        else:
            messages.warning(request, "Check your Form!")

    user_company = user.company
    context={'company':user_company,'company_form':CompanyUpdateForm(instance=user.company)}
    return render(request, "user/edit-company.html",context=context)


def company_detail(request,pk):
    company = Company.objects.get(pk=pk)
    context={'company':company}
    return render(request,'user/company_detail.html',context=context)

@login_required
def register_company(request):
    if request.method == 'POST':
        name =request.POST['company-name']
        region = request.POST['company-region']
        city = request.POST['company-city']
        document = request.FILES['company-document']
        company = Company.objects.create(
            employee=User.objects.get(pk=2),
            name=name,
            region=region,
            city=city,
            # document=document
        )
        return redirect('company-detail',company.pk)
    return render(request, "user/register_company.html")

@login_required
def company_list(request):
    user = request.user
    jobs = user.company.job_set.all()
    context = {'jobs':jobs}
    return render(request, "user/company_job_list.html",context=context)

@login_required
def company_job_application_list(request):
    company = request.user.company
    applications = Application.objects.filter(job__company=company)
    context={'job_apps':applications}
    return render(request,'user/company_job_application_list.html',context=context)

def company_job_application_list(request,pk):
    company = Company.objects.get(pk=pk)
    jobs = Job.objects.filter(company=company)
    context={'jobs':jobs}
    return render(request, 'jobsearch/job_listing.html',context=context)

@login_required
def change_status(request,status,pk):
    app = Application.objects.get(pk=pk)
    app.status = status
    app.save()
    return redirect('job-application-detail',pk)

def contact(request):
    return render(request, 'user/contact.html')
def about(request):
    return render(request,'user/about.html')
def handler_404_page(request,exception):
    return render(request,'404.html')
