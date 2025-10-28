from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [path('', views.home, name='home'),
               path('projects/', views.project_tree, name='projects_tree'),
               path('about/', views.about, name='about'),
               path('contacts/', views.contacts, name='contacts')] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)