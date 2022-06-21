from django.contrib import admin

from apps.user.models import Employer
from .models import Job,Company,Application
from django.contrib import messages
# from django.utils.translation import ngettext

# Register your models here.

class EmployerInline(admin.TabularInline):
    model = Employer

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title','company','category','type','salary')
    ordering = ('title',)
    search_fields = ('name', 'company')
    list_filter = ('type','category','education_level','region','company','education_level') 

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','employee','region','status','email')
    ordering = ('name',)
    search_fields = ('name','description')
    list_filter = ('status','region')
    
    @admin.action(description='approve selected Company')
    def approveSelectedCompany(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(request, ngettext(
            '%d company successfully approved',
            '%d companies were successfully approved',
            updated,
        ) % updated, messages.SUCCESS)

    actions = [approveSelectedCompany]
    # inlines = [EmployerInline]

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('user','job','status','created_at')
    ordering = ('user','job','created_at')
    search_fields = ('job__title','user__user__username')
    list_filter = ('job__company','created_at')

# Application
# admin.site.register(Application)