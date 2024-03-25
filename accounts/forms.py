from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm
from django.contrib.auth import get_user_model



class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'form-control'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your Email',
        'class': 'form-control'
    }))
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Your Password',
        'class': 'form-control'
    }))
    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput(attrs={
        
        'placeholder': 'Your Password Confirmation',
        'class': 'form-control'
    }))
    
    class Meta:
        model=get_user_model()
        fields=('username', 'email', 'password1', 'password2')


class SigninForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username or Email',
        'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'form-control'
    }))

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'description']

class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']
