from django.urls import path
from django.urls import re_path as url 
from .views import(
    jobs,
    job_details,
    applications,
    Apply,
)

urlpatterns = [
    path('all-jobs/', jobs, name='alljobs'),
    url(r'^job-details/(?P<id>\d+)/&', job_details, name='jobdetails'),
    url(r'^applications/', applications, name='applications'),
    url(r'^apply/(?P<id>\d+)/&', Apply.as_view(), name='apply')
]