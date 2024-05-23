from modeltranslation.translator import translator, TranslationOptions
from .models import Type


class TypeTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Type, TypeTranslationOptions)
