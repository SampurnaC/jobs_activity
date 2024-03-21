from django.shortcuts import render, redirect
from accounts.forms import SignupForm, SigninForm
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def signup(request):
    if request.method == "POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"New account created {user.username}")
            return redirect('/users/signin')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form=SignupForm()    
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/')


def custom_login(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = SigninForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect('/')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error) 

    form = SigninForm() 
    
    return render(
        request=request,
        template_name="accounts/signin.html", 
        context={'form': form}
        )
