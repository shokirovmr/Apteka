# Generated by Django 5.0.3 on 2024-05-28 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apteka", "0019_remove_pill_expiration_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="achievement",
            name="description",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Matni"
            ),
        ),
        migrations.AlterField(
            model_name="achievement",
            name="description_en",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Matni"
            ),
        ),
        migrations.AlterField(
            model_name="achievement",
            name="description_ru",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Matni"
            ),
        ),
        migrations.AlterField(
            model_name="achievement",
            name="description_uz",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Matni"
            ),
        ),
        migrations.AlterField(
            model_name="achievement",
            name="title",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Sarlavhasi"
            ),
        ),
        migrations.AlterField(
            model_name="achievement",
            name="title_en",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Sarlavhasi"
            ),
        ),
        migrations.AlterField(
            model_name="achievement",
            name="title_ru",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Sarlavhasi"
            ),
        ),
        migrations.AlterField(
            model_name="achievement",
            name="title_uz",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Sarlavhasi"
            ),
        ),
    ]
