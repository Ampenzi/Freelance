from django.contrib import admin
from .models import(
    Category,
    Job,
    Application
)

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display =['name', 'jobs']

admin.site.register(Category, CategoryAdmin)

class JobAdmin(admin.ModelAdmin):
    model = Job
    list_display = ['name', 'category', 'fee', 'completed']
    list_display_links = ['name']

admin.site.register(Job, JobAdmin)

class ApplicationAdmin(admin.ModelAdmin):
    model = Application
    list_display = ['applicant', 'bid', 'date', 'award']
    list_display_links = ['applicant']

admin.site.register(Application, ApplicationAdmin)