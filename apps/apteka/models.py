from django.core.validators import MinLengthValidator
from django.db import models

from apps.shared.models import AbstractBaseModel


class Type(AbstractBaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(published=True)


class Pill(AbstractBaseModel):
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    body = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    information = models.CharField(max_length=255, null=True, blank=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='pills')
    expiration_date = models.DateField()
    usage_url = models.URLField(max_length=1024)
    picture = models.ImageField(upload_to='pills/images/')
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    published = models.BooleanField(default=False)

    objects = models.Manager()
    published_objects = PublishedManager()

    def __str__(self):
        return f"{self.category}-{self.name}"


class Doctor(AbstractBaseModel):
    name = models.CharField(max_length=255)
    direction = models.CharField(max_length=255)
    call = models.CharField(max_length=20)
    body = models.TextField(null=True, blank=True)
    picture = models.ImageField(upload_to='doctors/images/')
    advices = models.ManyToManyField(Pill, related_name='doctors')
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

    def __str__(self):
        return self.name


class Commentary(models.Model):
    author = models.CharField(max_length=255)
    body = models.TextField()
    published = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Commentary by {self.author} on {self.published}"


class Entry(models.Model):
    fullname = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=20, validators=[MinLengthValidator(7)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname
