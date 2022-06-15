from django.urls import path
# from django.shortcuts import render
from . import views


urlpatterns = [
    path('',views.index,name='home'),
    path('job-detail',views.job_detail,name='job-detail'),
    path('job-list',views.job_list,name='job-list'),
    path('job-apply/<int:pk>',views.job_apply,name='job-apply'),
    path('job-post',views.job_post,name='job-post'),
    path('job-detail/<int:pk>',views.job_detail,name='job-detail'),
    path('job-application-list',views.job_application_list,name='job-application-list'),
    path('job-application-detail/<int:pk>',views.job_application_detail,name='job-application-detail'),

    
]