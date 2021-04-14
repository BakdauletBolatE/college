from django.contrib import admin
from .models import NewsCategory,NewsLikes,NewsPost,GalleryPost
# Register your models here.
admin.site.register(NewsCategory)
admin.site.register(GalleryPost)
admin.site.register(NewsPost)
admin.site.register(NewsLikes)