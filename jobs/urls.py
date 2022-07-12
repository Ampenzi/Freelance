from django.urls import path
from django.urls import re_path as url 
from .views import(
    jobs,
    JobDetails,
    applications,
    test
)

urlpatterns = [
    path('all-jobs/', jobs, name='alljobs'),
    url(r'^job-details/(?P<id>\d+)/&', JobDetails.as_view(), name='jobdetails'),
    url(r'^applications/', applications, name='applications'),
    path('test/', test),
]