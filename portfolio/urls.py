from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('projects/', views.ProjectsView.as_view(), name='projects'),
    path('resume/', views.ResumeView.as_view(), name='resume'),
    path('contact/', views.ContactView.as_view(), name='contact'),
] 