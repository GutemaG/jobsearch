from django.contrib import admin
from .models import Job,Company,Application
from django.contrib import messages
from django.utils.translation import ngettext

# Register your models here.



@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title','company','category','type','salary')
    ordering = ('title',)
    search_fields = ('name', 'company')

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','employee','region','status','email')
    ordering = ('name',)
    search_fields = ('name','description')
    
    @admin.action(description='approve selected Company')
    def approveSelectedCompany(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(request, ngettext(
            '%d company successfully approved',
            '%d companies were successfully approved',
            updated,
        ) % updated, messages.SUCCESS)

    actions = [approveSelectedCompany]

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('user','job','status','created_at')
    ordering = ('user','job','created_at')
    search_fields = ('user',)

# Application
# admin.site.register(Application)