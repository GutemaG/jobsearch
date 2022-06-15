from django.shortcuts import redirect, render
from apps.jobsearch.models import Company
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import User
# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect ('home')
        else:
            return redirect ('login')
    return render (request, 'user/login.html')

def logout_user(request):
    logout(request)
    return render (request, 'user/login.html')

from .forms import ApplicantCreationForm, UserCreationForm
def register(request):
    profile_form = UserCreationForm
    applicant_form = ApplicantCreationForm
    if request.method == "POST":
        profile_form = UserCreationForm(data=request.POST)
        applicant_form = ApplicantCreationForm(request.POST,request.FILES)
        if profile_form.is_valid() and applicant_form.is_valid():
            user = profile_form.save()
            applicant = applicant_form.save(commit=False)
            applicant.user = user
            applicant.save()
            messages.success(request, "You Successfully Registered!")
        else:
            print("invalid")
    
    context = {'form':profile_form,'applicant_form':applicant_form}
    return render (request, 'user/registration.html',context=context)

@login_required
def profile(request):
    user = request.user
    context={'user':user}
    return render(request, "user/profile.html",context=context)


def company_detail(request,pk):
    company = Company.objects.get(pk=pk)
    context={'company':company}
    return render(request,'user/company_detail.html',context=context)

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