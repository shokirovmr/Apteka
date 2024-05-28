from modeltranslation.translator import translator, TranslationOptions
from .models import Type, Pill, Achievement, Category, Doctor, Commentary


class TypeTranslationOptions(TranslationOptions):
    fields = ('name',)


class PillTranslationOPtions(TranslationOptions):
    fields = ('name', 'body', 'information', )


class DoctorTranslationOption(TranslationOptions):
    fields = ('direction', 'body',)


class AchievementTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class CommentaryTranslationOptions(TranslationOptions):
    fields = ('body',)


translator.register(Type, TypeTranslationOptions)
translator.register(Pill, PillTranslationOPtions)
translator.register(Achievement, AchievementTranslationOptions)
translator.register(Doctor, DoctorTranslationOption)
translator.register(Category, CategoryTranslationOptions)
translator.register(Commentary, CommentaryTranslationOptions)
