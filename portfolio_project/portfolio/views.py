from django.shortcuts import render
from .models import Project, Experience

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/project_list.html', {'projects': projects})

def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    experiences = Experience.objects.all()
    # print(experiences)
    return render(request, 'portfolio/about.html', {'experiences': experiences})
# Create your views here.
