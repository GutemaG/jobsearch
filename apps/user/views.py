from django.shortcuts import redirect, render
from apps.jobsearch.models import Company
from django.contrib.auth.models import User
# Create your views here.

def login(request):
    return render (request, 'user/login.html')

def register(request):
    return render (request, 'user/registration.html')

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