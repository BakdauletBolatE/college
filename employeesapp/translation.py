from modeltranslation.translator import register,TranslationOptions
from .models import *

@register(Government)
class GovernmentTranslationsOptions(TranslationOptions):
    fields = ('name','position')

@register(Employees)
class NewsCategoryTranslationsOptions(TranslationOptions):
    fields = ('name','position')



