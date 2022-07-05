from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def jobs(request):
    return render(request, 'jobs.html')

@login_required(login_url='login')
def job_details(request):
    return render(request, 'job-details.html')

@login_required(login_url='login')
def applications(request):
    return render(request, 'applications.html')