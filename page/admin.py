from page.models import Page
from django.contrib import admin
from .forms import PageForm

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'parent')
    list_editable = ('order', 'parent')
    list_filter = ('parent', 'page_type')
    form = PageForm


admin.site.register(Page, PageAdmin)
