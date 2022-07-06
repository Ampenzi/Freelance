
from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    bid = forms.FloatField()
    subject = forms.CharField()
    proposal = forms.Textarea()

    class Meta:
        model = Application
        fields = ('bid', 'subject','proposal')