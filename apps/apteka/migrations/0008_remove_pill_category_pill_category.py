# Generated by Django 5.0.3 on 2024-05-24 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apteka", "0007_alter_doctor_options_pill_popular"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pill",
            name="category",
        ),
        migrations.AddField(
            model_name="pill",
            name="category",
            field=models.ManyToManyField(blank=True, null=True, to="apteka.category"),
        ),
    ]
