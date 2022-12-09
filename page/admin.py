from page.models import Page
from django.contrib import admin



class PageAdmin(admin.ModelAdmin):

    list_display = ('name', 'order', 'parent')
    list_editable = ('order', 'parent')


admin.site.register(PageAdmin, Page)

