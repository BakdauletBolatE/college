from page.models import PageCategory, Widget, WidgetGalery, WidgetGalleryPhotos, WidgetPhoto,WidgetText,Page
from django.contrib import admin

# Register your models here.
admin.site.register(WidgetText)
admin.site.register(Widget)
admin.site.register(WidgetPhoto)
admin.site.register(WidgetGalleryPhotos)
admin.site.register(WidgetGalery)
admin.site.register(Page)
admin.site.register(PageCategory)