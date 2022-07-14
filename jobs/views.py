from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User
from django.db.models import Q 
# Create your views here.

from .models import (
    Job,
    Application
)


@login_required(login_url='login')
def jobs(request):
    jobs = Job.objects.filter(Q(assigned = False) | Q(completed=False))
    context={
        'jobs': jobs
    }
    return render(request, 'jobs.html', context)

class JobDetails(LoginRequiredMixin, View):
    def get(self, request, id):
        job = Job.objects.get(pk=id)
        return render(request, 'job-details.html', {'job':job})
    def post(self, request, id):
        user = User.objects.get(id = request.user.id)
        job = Job.objects.get(pk=id)
        obj = Application.objects.create(applicant=user, job=job, subject=job.name,)
        return redirect('applications')        
        

@login_required(login_url='login')
def applications(request):
    user = User.objects.get(pk=request.user.id)
    applications = Application.objects.filter(applicant=user)
    context= {
        'applications': applications
        }
    return render(request, 'applications.html', context )

def TnC(request):
    return render(request, 'faq.html')

def test(request):
    jobs = Job.objects.filter(Q(assigned = True) & Q(completed=False))
    context={
        'jobs': jobs
    }
    return render(request, 'apply.html', context)