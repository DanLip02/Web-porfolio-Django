from django.shortcuts import render
from .models import Project, Experience, UpdateLog, ContactInfo, get_social_links, list_buttons

# def project_list(request):
#     projects = Project.objects.all()
#     return render(request, 'portfolio/project_list.html', {'projects': projects})

def project_tree(request):
    projects = Project.objects.all()
    categories = {
        "work": projects.filter(category="work"),
        "university": projects.filter(category="university"),
        "personal": projects.filter(category="personal"),
    }
    return render(request, "portfolio/projects_tree.html", {"categories": categories, "projects": projects})

def home(request):
    updates = UpdateLog.objects.order_by('-created_at')[:5]
    return render(request, 'portfolio/home.html', {'updates': updates})

def about(request):
    experiences = Experience.objects.all()
    # print(experiences)
    return render(request, 'portfolio/about.html', {'experiences': experiences})

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
    context = {
        'social_links': social_links,
        'profile_photo_url': profile_photo_url,
        'buttons': buttons
        # 'short_description': short_description
    }
    return render(request, 'portfolio/contact.html', context)


# Create your views here.
