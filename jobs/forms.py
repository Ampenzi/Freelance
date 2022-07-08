
from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    bid = forms.FloatField()
    proposal = forms.Textarea()

    class Meta:
        model = Application
        fields = ('bid', 'proposal')