# Generated by Django 5.1.2 on 2024-10-23 06:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0007_alter_project_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="projects/"),
        ),
    ]
