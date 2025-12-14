from django.shortcuts import render
from .models import Project, Experience, UpdateLog, ContactInfo, get_social_links, list_buttons, get_cv
from django.conf import settings
import os
from django.http import HttpResponse, HttpResponseNotFound

# def project_list(request):
#     projects = Project.objects.all()
#     return render(request, 'portfolio/project_list.html', {'projects': projects})

def project_tree(request):
    projects = Project.objects.all()
    buttons = list_buttons()
    print("here my cv")
    categories = {
        "work": projects.filter(category="work"),
        "university": projects.filter(category="university"),
        "personal": projects.filter(category="personal"),
    }
    context = {"categories": categories,
               "projects": projects,
               "buttons": buttons,
    }
    return render(request, "portfolio/project_list.html", context)


def download_cv(request, filename):

    cv_folder = os.path.join(settings.MEDIA_ROOT, "my_cv")
    file_path = os.path.join(cv_folder, filename)

    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response

    return HttpResponseNotFound("File not found")

def home(request):
    updates = UpdateLog.objects.order_by('-created_at')[:5]
    buttons = list_buttons()
    context = {
        'updates' : updates,
        'buttons': buttons
        # 'short_description': short_description
    }
    return render(request, 'portfolio/home_dub.html', context)

def about(request):
    experiences = Experience.objects.all()
    buttons = list_buttons()
    context = {
        'experiences': experiences,
        'buttons': buttons,
        # 'short_description': short_description
    }
    return render(request, 'portfolio/about.html', context)

# def contacts(request):
#     contact_info = ContactInfo.objects.first()
#     social_link = SocialLink.objects.all()
#     # print(experiences)
#     return render(request, 'portfolio/contacts_.html', {'contact_info': contact_info})

def contacts(request):
    profile_photo_url = '/media/profile_photos/my_photo.png'

    # short_description = """I am a data analyst and data scientist in credit risk modeling.
    #                     Also I really love to learn new things and these web sited created by me to improve my knowledge in frontend developing"""

    buttons = list_buttons()

    social_links = get_social_links()
    cv = get_cv()
    context = {
        'social_links': social_links,
        'profile_photo_url': profile_photo_url,
        'buttons': buttons,
        "cv": cv
        # 'short_description': short_description
    }
    return render(request, 'portfolio/contact.html', context)


# Create your views here.
