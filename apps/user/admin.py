
# from email.headerregistry import Group
from django.contrib import admin
from django.contrib.auth.models import Group
from apps.jobsearch.models import Company
from .models import Employer, User,Applicant
from django.contrib import messages
from django.utils.translation import ngettext

# Register your models here.
admin.site.unregister(Group)
class ApplicantInline(admin.TabularInline):
    model = Applicant
    can_delete = False

class EmployerInline(admin.TabularInline):
    model = Employer

class CompanyInline(admin.StackedInline):
    model = Company
    fields=['name','status']
    can_delete = False


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','phone','region','user_type')
    ordering = ('username','first_name','last_name','user_type','created_at')
    search_fields = ('username','first_name','last_name','phone')
    list_filter = ('user_type','gender','region')
    fields = ['username','password',('first_name', 'last_name'),
            'email','gender','phone',('region','city'),'user_type',
            'date_joined'
            ]
            
    @admin.action(description='change user type to Employer')
    def changeUserToEmployer(self, request, queryset):
            updated = queryset.update(user_type="EMPLOYEE")
            self.message_user(request, ngettext(
            '%d User was successfully changed',
            '%d Users were successfully changed',
            updated,
        ) % updated, messages.SUCCESS)
    actions = [changeUserToEmployer]
    inlines = [ApplicantInline,EmployerInline]

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('user','education_level')
    ordering = ('user','created_at')
    search_fields = ('user__username','user__first_name','user__last_name','user__phone')
    list_filter =('education_level','user__employer__company')

@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('user','approved')
    ordering = ('user','approved')
    search_fields = ('user',)
    list_filter = ('approved','company',)    
    @admin.action(description='approve selected employer')
    def approveSelectedEmployer(self, request, queryset):
            updated = queryset.update(approved=True)
            self.message_user(request, ngettext(
            '%d Employer was successfully approved',
            '%d Employers were successfully approved',
            updated,
        ) % updated, messages.SUCCESS)

    actions = [approveSelectedEmployer]

    inlines = [CompanyInline]

