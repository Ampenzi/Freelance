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
    fee = models.FloatField(default=0.0, verbose_name='Salary')
    completed = models.BooleanField(default=False)
    added_on = models.DateField(auto_now_add=True)
    due = models.DateTimeField()

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
    def __Str__(self):
        return self.name

class Application(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)
    proposal = models.TextField()
    bid = models.FloatField(default=0.0)
    date = models.DateTimeField(auto_now_add=True)
    state = models.BooleanField(default=False)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'

    def __str__(self):
        self.applicant