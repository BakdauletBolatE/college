from django.contrib import admin
from .models import Government,Employees,EmployeesLikes
from modeltranslation.admin import TranslationAdmin
# Register your models here.

class GovernmentAdmin(TranslationAdmin):
    pass

class EmployeesAdmin(TranslationAdmin):
    pass

admin.site.register(Government,GovernmentAdmin)
admin.site.register(Employees,EmployeesAdmin)
admin.site.register(EmployeesLikes)