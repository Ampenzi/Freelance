from django.urls import path
from .views import(
    jobs,
    job_details,
    applications
)

urlpatterns = [
    path('all-jobs/', jobs, name='alljobs'),
    path('job-details/', job_details, name='jobdetails'),
    path('applications/', applications, name='applications'),
]