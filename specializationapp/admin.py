from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Specialization,SpecializationComment,SpecializationFaq,Section,SubSection,Qualification
# Register your models here.

class SpecializationFaqInline(admin.TabularInline):
    model = SpecializationFaq
    extra = 4


class SpecializationAdmin(TranslationAdmin):

     inlines = [
        SpecializationFaqInline,
    ]


admin.site.register(Specialization,SpecializationAdmin)


class SpecializationFaqAdmin(TranslationAdmin):
    list_filter = ('visible',)

admin.site.register(SpecializationFaq)




class SpecializationCommentAdmin(admin.ModelAdmin):
     list_filter = ('visible', )

admin.site.register(SpecializationComment,SpecializationCommentAdmin)


class SectionAdmin(TranslationAdmin):
    pass

admin.site.register(Section,SectionAdmin)

class SubSectionAdmin(TranslationAdmin):
    pass


admin.site.register(SubSection,SubSectionAdmin)

class QualificationAdmin(TranslationAdmin):
    pass

admin.site.register(Qualification,QualificationAdmin)

