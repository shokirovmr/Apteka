# Generated by Django 5.0.3 on 2024-05-25 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("apteka", "0012_alter_achievement_table_alter_category_table_and_more"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="pill",
            table="pills",
        ),
    ]
