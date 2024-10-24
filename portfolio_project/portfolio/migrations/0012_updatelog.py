# Generated by Django 5.1.2 on 2024-10-24 19:43

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0011_remove_experience_achievements_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="UpdateLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("created_at", models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
