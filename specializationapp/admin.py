from django.contrib import admin
from .models import Specialization,SpecializationComment,SpecializationFaq,Section,SubSection,Qualification
# Register your models here.

class SpecializationFaqInline(admin.TabularInline):
    model = SpecializationFaq
    extra = 4


class SpecializationAdmin(admin.ModelAdmin):

     inlines = [
        SpecializationFaqInline,
    ]


admin.site.register(Specialization,SpecializationAdmin)
admin.site.register(SpecializationFaq)




class SpecializationCommentAdmin(admin.ModelAdmin):
     list_filter = ('visible', )

admin.site.register(SpecializationComment,SpecializationCommentAdmin)


admin.site.register(Section)
admin.site.register(SubSection)
admin.site.register(Qualification)

