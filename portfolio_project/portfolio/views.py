from django.shortcuts import render
from .models import Project, Experience, UpdateLog, ContactInfo, SocialLink

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

def contacts(request):
    contact = ContactInfo.objects.all()
    media = SocialLink.objects.all()
    # print(experiences)
    return render(request, 'portfolio/contacts.html', {'contact': contact, 'media': media})
# Create your views here.
