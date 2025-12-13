from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [path('home/', views.home, name='home'),
               path('', views.home, name='home_index'),
               path('projects/', views.project_tree, name='projects_tree'),
               path('about/', views.about, name='about'),
               path('contact/', views.contacts, name='contact')] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)