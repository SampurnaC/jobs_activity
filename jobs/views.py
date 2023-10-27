from django.shortcuts import render, redirect
from .models import Job
# Create your views here.

def index(request):
    return render(request, 'jobs/index.html')


def home(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/home.html', {'jobs': jobs})
