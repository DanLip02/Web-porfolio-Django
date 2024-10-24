from django.shortcuts import render
from .models import Project, Experience, UpdateLog

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/project_list.html', {'projects': projects})

def home(request):
    updates = UpdateLog.objects.order_by('-created_at')[:5]
    return render(request, 'portfolio/home.html', {'updates': updates})

def about(request):
    experiences = Experience.objects.all()
    # print(experiences)
    return render(request, 'portfolio/about.html', {'experiences': experiences})
# Create your views here.
