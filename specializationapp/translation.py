from modeltranslation.translator import register,TranslationOptions
from .models import *

@register(Section)
class SectionTranslationsOptions(TranslationOptions):
    fields = ('name',)

@register(SubSection)

class SubSectionTranslationsOptions(TranslationOptions):
    fields = ('name',)


@register(Specialization)

class SpecializationTranslationsOptions(TranslationOptions):
    fields = ('name','desctiption')


@register(SpecializationFaq)

class SpecializationFaqTranslationsOptions(TranslationOptions):
    fields = ('question','answer')


@register(Qualification)

class SpecializationFaqTranslationsOptions(TranslationOptions):
    fields = ('name',)

