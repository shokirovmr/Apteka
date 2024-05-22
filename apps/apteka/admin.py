from django.contrib import admin
from .models import Type, Pill, Doctor, Rating, Partner, Achievement, Category


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Pill)
class PillAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'type', 'published')
    list_filter = ('published', 'type')
    search_fields = ('name', 'information')


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'direction', 'published')
    list_filter = ('published',)
    search_fields = ('name', 'direction')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('rank', 'pill')
    search_fields = ('pill__name',)


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('image_tag',)


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag')
    search_fields = ('title', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    filter_horizontal = ('pills',)
