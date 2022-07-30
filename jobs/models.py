from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Category name')
    jobs = models.IntegerField(default=0, verbose_name='Available jobs')
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name
    
class Job(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Job Category')
    name = models.CharField(max_length=50, verbose_name='Task name')
    details = models.TextField()
    fee = models.CharField(max_length=20, verbose_name='Salary')
    completed = models.BooleanField(default=False)
    added_on = models.DateField(auto_now_add=True)
    assigned = models.BooleanField(default=False)
    due = models.DateTimeField()

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
    def __Str__(self):
        return self.name

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    award = models.BooleanField(default=False, verbose_name='Assign Work')

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'

    def __str__(self):
        return self.job.name 
    
    def get_job(self):
        job = self.job.name
        return(job)

    def get_job_state(self):
        state = self.job.completed
        return state

class Submission(models.Model):
    job = models.CharField(max_length=50)
    doc = models.FileField(upload_to='uploads/')
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.job