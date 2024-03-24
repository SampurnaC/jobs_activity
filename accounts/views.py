from django.shortcuts import render, redirect
from accounts.forms import SignupForm, SigninForm, UserUpdateForm
from django.contrib.auth import get_user_model, login, logout, authenticate, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage

from .tokens import account_activation_token


def activateEmail(request, user, to_email):
    mail_subject = 'Activate your user account.'
    message = render_to_string('accounts/template_activate_account.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
            received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending confirmation email to {to_email}, check if you typed it correctly.')

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('signin')
    else:
        messages.error(request, 'Activation link is invalid!')
    
    return redirect('/')

def signup(request):
    if request.method == "POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active=False
            user.save()
            activateEmail(request,user,form.cleaned_data.get('email'))
            # login(request, user)
            # messages.success(request, f"New account created {user.username}")
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

def profile(request, username):
    if request.method == 'POST':
        user = request.user
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            user_form = form.save()

            messages.success(request, f'{user_form}, Your profile has been updated!')
            return redirect('profile', user_form.username)

        for error in list(form.errors.values()):
            messages.error(request, error)
    user = get_user_model().objects.filter(username=username).first()
    if user:
        form = UserUpdateForm(instance=user)
        form.fields['description'].widget.attrs = {'rows': 1}
        return render(request, 'accounts/profile.html', context={'form': form})

    return redirect("/")
