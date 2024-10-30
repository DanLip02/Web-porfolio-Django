from django.utils import timezone
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', null=True)  # Изображение
    progress = models.PositiveIntegerField(default=0)  # Новое поле для процента выполнения
    link = models.URLField(max_length=200, blank=True)  # Ссылка на проект

    def __str__(self):
            return self.title

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


class SocialLink(models.Model):
    platform_name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='social_icons/')  # Иконка соцсети
    url = models.URLField()
    contact_info = models.ForeignKey(ContactInfo, related_name='social_links', on_delete=models.CASCADE)

    def __str__(self):
        return self.platform_name

# Create your models here.
