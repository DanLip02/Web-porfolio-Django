from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone
from .models import Project, Experience, UpdateLog

# Отслеживание добавления/изменения проекта
@receiver(post_save, sender=Project)
def log_project_save(sender, instance, created, **kwargs):
    if created:
        UpdateLog.objects.create(
            title="New Project Added",
            description=f"A new project '{instance.title}' was added on {timezone.now()}."
        )
    else:
        UpdateLog.objects.create(
            title="Project Updated",
            description=f"The project '{instance.title}' was updated on {timezone.now().date()}."
        )

# Отслеживание удаления проекта
@receiver(post_delete, sender=Project)
def log_project_delete(sender, instance, **kwargs):
    UpdateLog.objects.create(
        title="Project Deleted",
        description=f"The project '{instance.title}' was deleted."
    )

# Отслеживание изменений в разделе AboutMe
@receiver(post_save, sender=Experience)
def log_aboutme_save(sender, instance, created, **kwargs):
    if created:
        UpdateLog.objects.create(
            title="About Me Section Added",
            description=f"New information was added to the 'About Me' section."
        )
    else:
        UpdateLog.objects.create(
            title="About Me Section Updated",
            description=f"The '{instance.institution} - {instance.role}' section was updated."
        )