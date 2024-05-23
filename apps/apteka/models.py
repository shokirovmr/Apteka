from django.db import models

from apps.shared.models import AbstractBaseModel


class Type(AbstractBaseModel):
    name = models.CharField(max_length=255)


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(published=True)


class Pill(AbstractBaseModel):
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    information = models.CharField(max_length=255)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='pills')
    expiration_date = models.DateField()
    usage_url = models.URLField(max_length=1024)
    picture = models.ImageField(upload_to='pills/images/')
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    published = models.BooleanField(default=False)

    objects = models.Manager()
    published_objects = PublishedManager()


class Doctor(AbstractBaseModel):
    name = models.CharField(max_length=255)
    direction = models.CharField(max_length=255)
    call = models.CharField(max_length=20)
    body = models.TextField()
    picture = models.ImageField(upload_to='doctors/images/')
    tavsiflari_dori = models.CharField(max_length=255)
    published = models.BooleanField(default=False)

    objects = models.Manager()
    published_objects = PublishedManager()


class Rating(models.Model):
    rank = models.IntegerField()
    pill = models.ForeignKey(Pill, on_delete=models.CASCADE, related_name='ratings')


class Partner(models.Model):
    image = models.ImageField(upload_to='partners/images/')


class Achievement(models.Model):
    image = models.ImageField(upload_to='achievements/images/')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class Category(models.Model):
    name = models.CharField(max_length=255)
