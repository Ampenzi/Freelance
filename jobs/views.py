from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User
# Create your views here.

from .models import (
    Job,
    Application
)

from .forms import ApplicationForm

@login_required(login_url='login')
def jobs(request):
    jobs = Job.objects.all()
    context={
        'jobs': jobs
    }
    return render(request, 'jobs.html', context)

@login_required(login_url='login')
def job_details(request, id):
    job = Job.objects.get(pk=id)
    return render(request, 'job-details.html', {'job':job})

@login_required(login_url='login')
def applications(request):
    user = User.objects.get(pk=request.user.id)
    applications = Application.objects.filter(applicant=user)
    context= {
        'applications': applications
        }
    return render(request, 'applications.html', context )

class Apply(LoginRequiredMixin, View):
    def get(self, request, id):
        job = Job.objects.get(pk=id)
        form = ApplicationForm()
        context = {
            'form': form,
            'job': job
            }
        return render(request, 'apply.html', context)
    def post(self, request, id):
        job = Job.objects.get(pk=id)
        user = User.objects.get(pk=request.user.id)
        form = ApplicationForm(request.POST)
        if form.is_valid:
            form.instance.applicant = user
            form.instance.job = job
            form.instance.subject = job.name
            form.save()
            return redirect('applications')
        return render(request, 'apply.html')

def TnC(request):
    return render(request, 'faq.html')