# Generated by Django 5.1.2 on 2024-10-22 18:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0004_alter_project_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="project",
            old_name="project_url",
            new_name="link",
        ),
    ]