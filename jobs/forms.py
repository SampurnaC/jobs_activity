from django import forms
from .models import Job
from django.contrib.auth.models import User

class JobForm(forms.ModelForm):
    class Meta:
        model= Job
        fields=['title', 'companyname', 'url', 'status', 'extra_note']
        widgets={
            'title': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'Enter your job title'}),
            'companyname': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'Enter the company name'}),
            'url': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'Enter job URL',}),
            'status': forms.Select(attrs= {'class': 'form-control', 'style': 'appearance: auto; width: 200px;'}),

            'extra_note': forms.Textarea(attrs= {'class': 'form-control', 'rows': 6, 'cols': 15, 'placeholder': 'Add extra note here. Leave it blank if there is nothing.',}),
        }
