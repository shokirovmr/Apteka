# Generated by Django 5.0.3 on 2024-05-28 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("apteka", "0026_achievement_created_at_achievement_updated_at"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="achievement",
            options={
                "ordering": ["-created_at"],
                "verbose_name": "Muvaffaqiyat",
                "verbose_name_plural": "Muvaffaqiyatlar",
            },
        ),
    ]
