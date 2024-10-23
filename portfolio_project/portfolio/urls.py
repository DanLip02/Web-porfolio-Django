from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [path('', views.home, name='home'),
               path('projects/', views.project_list, name='project_list'),
               path('about/', views.about, name='about')] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)