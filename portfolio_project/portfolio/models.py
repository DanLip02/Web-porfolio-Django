from django.utils import timezone
from django.db import models
import os
from django.conf import settings

SOCIAL_URLS = {
    'github_icon': 'https://github.com/DanLip02',
    'linked_icon': 'https://www.linkedin.com/in/danila-lipatov-57019b34a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app',
    'telegram_icon': 'https://t.me/danilalip2002',
    'twitch_icon': 'https://www.twitch.tv/mr_cringulya',
    'pastebin_icon': 'https://pastebin.com/u/Danila_lipatov'
}

BUTTON_URLS = {
    "home": "/home/",
    "about": "/about/",
    "projects": "/projects/",
    "contact": "/contact/",
}


class Project(models.Model):
    CATEGORY_CHOICES = [
        ("work", "Рабочие"),
        ("university", "Вузовские"),
        ("personal", "Личные/пэт"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    # image = models.ImageField(upload_to='projects/', null=True, blank=True)
    progress = models.PositiveIntegerField(default=0)
    link = models.URLField(max_length=200, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES,  default='personal')

    def __str__(self):
        return f"{self.title} ({self.category})"

class Experience(models.Model):
    EXPERIENCE_TYPES = [
        ('education', 'Обучение'),
        ('work', 'Место работы'),
    ]
    type = models.CharField(max_length=10, choices=EXPERIENCE_TYPES, default='education')  # Тип: обучение или работа
    institution = models.CharField(max_length=255)  # Учебное заведение или компания
    role = models.CharField(max_length=255)  # Специальность или должность
    # description = models.TextField()  # Что делал
    # technologies = models.TextField()  # Стек технологий
    # achievements = models.TextField(blank=True, null=True)  # Достижения
    start_date = models.DateField()  # Начало
    end_date = models.DateField(blank=True, null=True)  # Окончание (может быть пустым, если работа продолжается)

    def __str__(self):
        print(f"{self.institution} - {self.role}")
        return f"{self.institution} - {self.role}"


class Technology(models.Model):
    experience = models.ForeignKey(Experience, related_name='technologies', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Achievement(models.Model):
    experience = models.ForeignKey(Experience, related_name='achievements', on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.description

class UpdateLog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title


class ContactInfo(models.Model):
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    short_description = models.TextField(blank=True)

    def __str__(self):
        return self.short_description

# class SocialLink(models.Model):
#     platform_name = models.CharField(max_length=50)
#     icon = models.ImageField(upload_to='social_icons/')
#     url = models.URLField()
#     contact_info = models.ForeignKey(ContactInfo, related_name='social_links', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.platform_name

def get_social_links():
    folder = os.path.join(settings.MEDIA_ROOT, 'social_icons')
    links = []
    for filename in os.listdir(folder):
        name, ext = os.path.splitext(filename)
        url = SOCIAL_URLS.get(name.lower())
        if url:
            links.append({
                'name': name.capitalize(),
                'icon_url': f'{settings.MEDIA_URL}social_icons/{filename}',
                'url': url,
            })
    return links

def list_buttons():
    folder = os.path.join(settings.MEDIA_ROOT, "buttons")
    buttons = []
    for filename in os.listdir(folder):
        if os.path.isfile(os.path.join(folder, filename)):
            name, ext = os.path.splitext(filename)
            buttons.append({
                "name": name.capitalize(),
                "img_url": f"{settings.MEDIA_URL}buttons/{filename}",
                "link": f"/{name.lower()}/",
            })
    return buttons

def get_cv():
    folder = os.path.join(settings.BASE_DIR, 'media', 'my_cv')

    if not os.path.exists(folder):
        folder = os.path.join(settings.MEDIA_ROOT, 'my_cv')

    if not os.path.exists(folder):
        return None

    for file in os.listdir(folder):
        if file.lower().endswith('.pdf'):
            return {
                'file_url': f'/media/my_cv/{file}',
                'file_name': file,
                'display_name': 'My CV'
            }

    return None

# Create your models here.
