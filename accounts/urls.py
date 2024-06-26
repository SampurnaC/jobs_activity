from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import SigninForm

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    # path('signin/', auth_views.LoginView.as_view(template_name='accounts/signin.html', authentication_form=SigninForm), name='signin'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='accounts/signout.html'), name='logout'),
    path('signin/', views.custom_login, name='signin'),
    path('logout/', views.custom_logout, name='logout'),
    path('profile/<username>/', views.profile, name='profile'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('password_change', views.password_change, name='password-change'),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path('reset/<uidb64>/<token>', views.passwordResetConfirm, name='password_reset_confirm'),


]
