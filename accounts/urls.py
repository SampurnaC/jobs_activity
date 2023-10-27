from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
# from .forms import SigninForm

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    # path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=SigninForm), name='login'),
    # path('logout/', views.logout_user, name='logout'),
   


]
