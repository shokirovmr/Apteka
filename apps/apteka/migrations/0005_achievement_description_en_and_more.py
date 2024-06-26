# Generated by Django 5.0.3 on 2024-05-23 09:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apteka", "0004_type_name_en_type_name_ru_type_name_uz"),
    ]

    operations = [
        migrations.AddField(
            model_name="achievement",
            name="description_en",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="achievement",
            name="description_ru",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="achievement",
            name="description_uz",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="achievement",
            name="title_en",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="achievement",
            name="title_ru",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="achievement",
            name="title_uz",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="category",
            name="name_en",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="category",
            name="name_ru",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="category",
            name="name_uz",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="doctor",
            name="body_en",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="doctor",
            name="body_ru",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="doctor",
            name="body_uz",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="doctor",
            name="direction_en",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="doctor",
            name="direction_ru",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="doctor",
            name="direction_uz",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="pill",
            name="body_en",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="pill",
            name="body_ru",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="pill",
            name="body_uz",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="pill",
            name="information_en",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="pill",
            name="information_ru",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="pill",
            name="information_uz",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="pill",
            name="name_en",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="pill",
            name="name_ru",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="pill",
            name="name_uz",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="pill",
            name="type_en",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pills",
                to="apteka.type",
            ),
        ),
        migrations.AddField(
            model_name="pill",
            name="type_ru",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pills",
                to="apteka.type",
            ),
        ),
        migrations.AddField(
            model_name="pill",
            name="type_uz",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pills",
                to="apteka.type",
            ),
        ),
        migrations.AlterField(
            model_name="doctor",
            name="body",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="pill",
            name="body",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="pill",
            name="information",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
