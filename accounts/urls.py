from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import SigninForm

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', auth_views.LoginView.as_view(template_name='accounts/signin.html', authentication_form=SigninForm), name='signin'),
    # path('logout/', views.logout_user, name='logout'),
   


]
