from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import Type, Pill, Doctor, Rating, Partner, Achievement, Category, Commentary, Entry


@admin.register(Type)
class TypeAdmin(TabbedTranslationAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Pill)
class PillAdmin(TabbedTranslationAdmin):
    list_display = ('name', 'price', 'type', 'published')
    list_filter = ('published', 'type')
    search_fields = ('name', 'information')


@admin.register(Doctor)
class DoctorAdmin(TabbedTranslationAdmin):
    list_display = ('name', 'direction', 'published')
    list_filter = ('published',)
    search_fields = ('name', 'direction')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('rank', 'pill')
    search_fields = ('pill__name',)


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('image',)


@admin.register(Achievement)
class AchievementAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'image')
    search_fields = ('title', 'description')


@admin.register(Category)
class CategoryAdmin(TabbedTranslationAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'published')
    search_fields = ('author', 'body')
    list_filter = ('published',)


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'phonenumber', 'created_at')
    search_fields = ('fullname', 'phonenumber')
    list_filter = ('created_at',)
