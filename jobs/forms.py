from django import forms
from .models import Job
from django.contrib.auth.models import User

class JobForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your job title',
        'class': 'form-control'
    }))
    companyname = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter the company name',
        'class': 'form-control'
    }))
    url = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter job URL',
        'class': 'form-control'
    }))
    class Meta:
        model= Post
        fields=['title', 'companyname', 'url']
