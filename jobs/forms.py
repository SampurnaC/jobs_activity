from django import forms
from .models import Job
from django.contrib.auth.models import User

class JobForm(forms.ModelForm):
    class Meta:
        model= Job
        fields=['title', 'companyname', 'url', 'status']
        # title = forms.CharField(widget=forms.TextInput(attrs={
        #     'placeholder': 'Enter your job title',
        #     'class': 'form-control'
        # }))
        # companyname = forms.CharField(widget=forms.TextInput(attrs={
        #     'placeholder': 'Enter the company name',
        #     'class': 'form-control'
        # }))
        # url = forms.CharField(widget=forms.TextInput(attrs={
        #     'placeholder': 'Enter job URL',
        #     'class': 'form-control'
        # }))
        
        widgets={
            'title': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'Enter your job title'}),
            'companyname': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'Enter the company name'}),
            'url': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'Enter job URL',}),
            'status': forms.Select(attrs= {'class': 'form-control', 'style': 'appearance: auto; width: 200px;'})

        }
