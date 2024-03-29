from django.contrib import admin
from .models import(
    Category,
    Job,
    Application,
    Submission,
)

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display =['name', 'jobs']

admin.site.register(Category, CategoryAdmin)

class JobAdmin(admin.ModelAdmin):
    model = Job
    list_display = ['name', 'category', 'fee', 'completed', 'assigned']
    list_display_links = ['name']

admin.site.register(Job, JobAdmin)

class ApplicationAdmin(admin.ModelAdmin):
    model = Application
    list_display = ['applicant', 'subject', 'date', 'award']
    list_display_links = ['applicant']

admin.site.register(Application, ApplicationAdmin)

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['job', 'date', 'doc']

admin.site.register(Submission, SubmissionAdmin)