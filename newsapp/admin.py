from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import NewsCategory, NewsLikes, NewsPost, GalleryPost

# Register your models here.
admin.site.register(NewsCategory)
admin.site.register(GalleryPost)
admin.site.register(NewsLikes)


# Apply summernote to all TextField in model.
class NewsPostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('description_ru', 'description', 'description_kk', 'description_en')


admin.site.register(NewsPost, NewsPostAdmin)
