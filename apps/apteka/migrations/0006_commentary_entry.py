# Generated by Django 5.0.3 on 2024-05-24 10:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apteka", "0005_achievement_description_en_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Commentary",
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
                ("author", models.CharField(max_length=255)),
                ("body", models.TextField()),
                ("published", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Entry",
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
                ("fullname", models.CharField(max_length=255)),
                (
                    "phonenumber",
                    models.CharField(
                        max_length=20,
                        validators=[django.core.validators.MinLengthValidator(7)],
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]