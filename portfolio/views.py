from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name = 'portfolio/home.html'

class ProjectsView(TemplateView):
    template_name = 'portfolio/projects.html'

class ResumeView(TemplateView):
    template_name = 'portfolio/resume.html'

class ContactView(TemplateView):
    template_name = 'portfolio/contact.html'
