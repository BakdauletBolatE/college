from django.contrib import admin
from .models import Government,Employees,EmployeesLikes
# Register your models here.


admin.site.register(Government)
admin.site.register(Employees)
admin.site.register(EmployeesLikes)