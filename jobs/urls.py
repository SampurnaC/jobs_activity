from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jobs/', views.home, name='home'),
    path('jobs/new/', views.new, name='new'),
    path('jobs/edit/<int:id>/', views.edit, name='edit'),
    path('jobs/delete/<int:id>', views.delete, name='delete'),
    path('jobs/<int:id>', views.show_job, name='show'),
    path('jobs/search_job', views.search_job, name='search-job'),

]
