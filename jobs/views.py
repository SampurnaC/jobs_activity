from django.shortcuts import render, redirect
from .models import Job
from .forms import JobForm
# Create your views here.

def index(request):
    return render(request, 'jobs/index.html')


def home(request):
    current_user=request.user
    jobs = Job.objects.filter(author_id=current_user.id)
    return render(request, 'jobs/home.html', {'jobs': jobs})

def new(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            form.instance.author=request.user
            post=form.save()
            post.save()
            return redirect('/')
    else:
        form=JobForm()
    return render(request, 'jobs/new.html', {'form': form})
