from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jobs/', views.home, name='home'),
    path('jobs/new/', views.new, name='new'),
    path('jobs/edit/<int:id>/', views.edit, name='edit'),

]
