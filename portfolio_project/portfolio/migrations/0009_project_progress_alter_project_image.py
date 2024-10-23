# Generated by Django 5.1.2 on 2024-10-23 08:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0008_alter_project_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="progress",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.ImageField(null=True, upload_to="projects/"),
        ),
    ]
