from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import NewsCategory, NewsLikes, NewsPost, GalleryPost, File

# Register your models here.
admin.site.register(NewsCategory)
admin.site.register(GalleryPost)
admin.site.register(NewsLikes)


class FileTabularInline(admin.TabularInline):
    model = File
# Apply summernote to all TextField in model.
class NewsPostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    inlines = [FileTabularInline]
    summernote_fields = ('description_ru', 'description', 'description_kk', 'description_en')


admin.site.register(NewsPost, NewsPostAdmin)
