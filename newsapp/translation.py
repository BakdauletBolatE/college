from modeltranslation.translator import register,TranslationOptions
from .models import *

@register(NewsPost)
class NewsPostTranslationsOptions(TranslationOptions):
    fields = ('title','description')

@register(NewsCategory)
class NewsCategoryTranslationsOptions(TranslationOptions):
    fields = ('name',)



