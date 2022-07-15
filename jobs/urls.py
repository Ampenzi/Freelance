from django.urls import path
from django.urls import re_path as url 
from .views import(
    jobs,
    JobDetails,
    SubmissionView,
    applications,
    
)

urlpatterns = [
    path('all-jobs/', jobs, name='alljobs'),
    url(r'^job-details/(?P<id>\d+)/&', JobDetails.as_view(), name='jobdetails'),
    url(r'^applications/', applications, name='applications'),
    url(r'^submit/(?P<pid>\d+)/&', SubmissionView.as_view(), name='submit'),
]