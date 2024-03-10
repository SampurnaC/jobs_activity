from django.shortcuts import render, redirect, get_object_or_404
from .models import Job
from .forms import JobForm
from django.contrib.auth.decorators import login_required
import datetime
from .tasks import test_func
from django.http import HttpResponse

def test(request):
    test_func.delay()
    return HttpResponse("coming from views")

def index(request):
    today = datetime.date.today()
    year = today.year
    return render(request, 'jobs/index.html', {'year': year})


def home(request):
    current_user=request.user
    jobs = Job.objects.filter(author_id=current_user.id).order_by('-created_at')
    return render(request, 'jobs/home.html', {'jobs': jobs})

def search_job(request):
    return render(request, 'jobs/search_job.html')

@login_required
def new(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            form.instance.author=request.user
            post=form.save()
            post.save()
            return redirect('/jobs')
    else:
        form=JobForm()
    return render(request, 'jobs/new.html', {'form': form})

@login_required
def edit(request, id):
    current_user=request.user
    job = Job.objects.filter(author_id=current_user.id).get(id=id)
    form = JobForm(request.POST or None, instance=job)
    if form.is_valid():
        form.save()
        return redirect('/jobs')
    return render(request, 'jobs/edit.html', {'job': job, 'form': form})

@login_required
def delete(request, id):
    current_user=request.user
    job=Job.objects.filter(author_id=current_user.id).get(id=id)
    job.delete()
    return redirect('/jobs')

@login_required
def show_job(request, id):
    current_user=request.user
    job=Job.objects.filter(author_id=current_user.id).get(id=id)
    context={'job': job}

    return render(request, 'jobs/show.html', context)
