from django.urls import path
from django.shortcuts import render
from . import views


urlpatterns = [
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('create-new-account/',views.register,name='create-account'),
    path('profile/',views.profile,name='profile'),
    path('register-your-company/',views.register_company,name='register-company'),
    path('company-detail/<int:pk>/',views.company_detail,name='company-detail'),
    path('your-company/',views.user_company,name='your-company'),
    path('edit-company/',views.edit_company,name='edit-company'),
]
