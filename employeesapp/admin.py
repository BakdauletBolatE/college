from django.contrib import admin
from django.contrib.admin import TabularInline
from .models import Government,Employees,EmployeesLikes, Leсture
from modeltranslation.admin import TranslationAdmin
# Register your models here.

class GovernmentAdmin(TranslationAdmin):
    pass


class LecturesTabularInline(TabularInline):
    model = Leсture

class EmployeesAdmin(TranslationAdmin):
    inlines = [LecturesTabularInline]

admin.site.register(Government,GovernmentAdmin)
admin.site.register(Employees,EmployeesAdmin)
admin.site.register(EmployeesLikes)