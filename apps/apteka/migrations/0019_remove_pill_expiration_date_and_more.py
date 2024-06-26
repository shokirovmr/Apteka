# Generated by Django 5.0.3 on 2024-05-27 13:36

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apteka", "0018_alter_achievement_options_alter_commentary_options_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pill",
            name="expiration_date",
        ),
        migrations.AlterField(
            model_name="achievement",
            name="description",
            field=models.CharField(max_length=255, verbose_name="Matni"),
        ),
        migrations.AlterField(
            model_name="achievement",
            name="description_en",
            field=models.CharField(max_length=255, null=True, verbose_name="Matni"),
        ),
        migrations.AlterField(
            model_name="achievement",
            name="description_ru",
            field=models.CharField(max_length=255, null=True, verbose_name="Matni"),
        ),
        migrations.AlterField(
            model_name="achievement",
            name="description_uz",
            field=models.CharField(max_length=255, null=True, verbose_name="Matni"),
        ),
        migrations.AlterField(
            model_name="achievement",
            name="image",
            field=models.ImageField(
                upload_to="achievements/images/", verbose_name="Rasmi"
            ),
        ),
        migrations.AlterField(
            model_name="achievement",
            name="title",
            field=models.CharField(max_length=255, verbose_name="Sarlavhasi"),
        ),
        migrations.AlterField(
            model_name="achievement",
            name="title_en",
            field=models.CharField(
                max_length=255, null=True, verbose_name="Sarlavhasi"
            ),
        ),
        migrations.AlterField(
            model_name="achievement",
            name="title_ru",
            field=models.CharField(
                max_length=255, null=True, verbose_name="Sarlavhasi"
            ),
        ),
        migrations.AlterField(
            model_name="achievement",
            name="title_uz",
            field=models.CharField(
                max_length=255, null=True, verbose_name="Sarlavhasi"
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=255, verbose_name="Nomi"),
        ),
        migrations.AlterField(
            model_name="category",
            name="name_en",
            field=models.CharField(max_length=255, null=True, verbose_name="Nomi"),
        ),
        migrations.AlterField(
            model_name="category",
            name="name_ru",
            field=models.CharField(max_length=255, null=True, verbose_name="Nomi"),
        ),
        migrations.AlterField(
            model_name="category",
            name="name_uz",
            field=models.CharField(max_length=255, null=True, verbose_name="Nomi"),
        ),
        migrations.AlterField(
            model_name="commentary",
            name="author",
            field=models.CharField(max_length=255, verbose_name="Avtor"),
        ),
        migrations.AlterField(
            model_name="commentary",
            name="body",
            field=models.TextField(verbose_name="Text"),
        ),
        migrations.AlterField(
            model_name="commentary",
            name="published",
            field=models.DateField(
                auto_now_add=True, verbose_name="Izoh yozilgan vaqt"
            ),
        ),
        migrations.AlterField(
            model_name="doctor",
            name="advices",
            field=models.ManyToManyField(
                related_name="doctors",
                to="apteka.pill",
                verbose_name="Tavsiya qilgan dorilari",
            ),
        ),
        migrations.AlterField(
            model_name="doctor",
            name="body",
            field=models.TextField(
                blank=True, null=True, verbose_name="Qo'shimcha ma'lumotlar"
            ),
        ),
        migrations.AlterField(
            model_name="doctor",
            name="body_en",
            field=models.TextField(
                blank=True, null=True, verbose_name="Qo'shimcha ma'lumotlar"
            ),
        ),
        migrations.AlterField(
            model_name="doctor",
            name="body_ru",
            field=models.TextField(
                blank=True, null=True, verbose_name="Qo'shimcha ma'lumotlar"
            ),
        ),
        migrations.AlterField(
            model_name="doctor",
            name="body_uz",
            field=models.TextField(
                blank=True, null=True, verbose_name="Qo'shimcha ma'lumotlar"
            ),
        ),
        migrations.AlterField(
            model_name="doctor",
            name="call",
            field=models.CharField(max_length=20, verbose_name="Telefon raqami"),
        ),
        migrations.AlterField(
            model_name="doctor",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Qo'shilgan vaqt"
            ),
        ),
        migrations.AlterField(
            model_name="doctor",
            name="direction",
            field=models.CharField(max_length=255, verbose_name="Yo'nalishi"),
        ),
        migrations.AlterField(
            model_name="doctor",
            name="direction_en",
            field=models.CharField(
                max_length=255, null=True, verbose_name="Yo'nalishi"
            ),
        ),
        migrations.AlterField(
            model_name="doctor",
            name="direction_ru",
            field=models.CharField(
                max_length=255, null=True, verbose_name="Yo'nalishi"
            ),
        ),
        migrations.AlterField(
            model_name="doctor",
            name="direction_uz",
            field=models.CharField(
                max_length=255, null=True, verbose_name="Yo'nalishi"
            ),
        ),
        migrations.AlterField(
            model_name="doctor",
            name="name",
            field=models.CharField(max_length=255, verbose_name="Ism-familiya"),
        ),
        migrations.AlterField(
            model_name="doctor",
            name="picture",
            field=models.ImageField(upload_to="doctors/images/", verbose_name="Rasmi"),
        ),
        migrations.AlterField(
            model_name="doctor",
            name="published",
            field=models.BooleanField(
                default=False, verbose_name="Saytda ko'rinsinmi?"
            ),
        ),
        migrations.AlterField(
            model_name="doctor",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, verbose_name="O'zgartirilgan vaqt"
            ),
        ),
        migrations.AlterField(
            model_name="entry",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Yuborilgan vaqt"
            ),
        ),
        migrations.AlterField(
            model_name="entry",
            name="fullname",
            field=models.CharField(max_length=255, verbose_name="Ism-familiya"),
        ),
        migrations.AlterField(
            model_name="entry",
            name="phonenumber",
            field=models.CharField(
                max_length=20,
                validators=[django.core.validators.MinLengthValidator(7)],
                verbose_name="Telefon raqam",
            ),
        ),
        migrations.AlterField(
            model_name="partner",
            name="image",
            field=models.ImageField(
                upload_to="partners/images/", verbose_name="Hamkor logosi"
            ),
        ),
        migrations.AlterField(
            model_name="pill",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Qo'shilgan vaqt"
            ),
        ),
        migrations.AlterField(
            model_name="pill",
            name="discount_price",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=10,
                null=True,
                verbose_name="Chegirma narxi",
            ),
        ),
        migrations.AlterField(
            model_name="pill",
            name="information",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Tarkibi"
            ),
        ),
        migrations.AlterField(
            model_name="pill",
            name="information_en",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Tarkibi"
            ),
        ),
        migrations.AlterField(
            model_name="pill",
            name="information_ru",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Tarkibi"
            ),
        ),
        migrations.AlterField(
            model_name="pill",
            name="information_uz",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Tarkibi"
            ),
        ),
        migrations.AlterField(
            model_name="pill",
            name="picture",
            field=models.ImageField(upload_to="pills/images/", verbose_name="Rasmi"),
        ),
        migrations.AlterField(
            model_name="pill",
            name="popular",
            field=models.BooleanField(default=False, verbose_name="Ommabopmi?"),
        ),
        migrations.AlterField(
            model_name="pill",
            name="price",
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name="Narxi"
            ),
        ),
        migrations.AlterField(
            model_name="pill",
            name="published",
            field=models.BooleanField(
                default=False, verbose_name="Saytda ko'rinsinmi?"
            ),
        ),
        migrations.AlterField(
            model_name="pill",
            name="rank",
            field=models.IntegerField(
                choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)],
                default=5,
                verbose_name="Reyting",
            ),
        ),
        migrations.AlterField(
            model_name="pill",
            name="type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pills",
                to="apteka.type",
                verbose_name="Dori turi",
            ),
        ),
        migrations.AlterField(
            model_name="pill",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, verbose_name="O'zgartirilgan vaqt"
            ),
        ),
        migrations.AlterField(
            model_name="pill",
            name="usage_url",
            field=models.URLField(
                blank=True,
                max_length=1024,
                null=True,
                verbose_name="Foydalanish video manzili",
            ),
        ),
        migrations.AlterField(
            model_name="type",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Qo'shilgan vaqt"
            ),
        ),
        migrations.AlterField(
            model_name="type",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, verbose_name="O'zgartirilgan vaqt"
            ),
        ),
    ]
