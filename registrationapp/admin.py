from django.contrib import admin
from .models import App, EduProgram
from django.utils.safestring import mark_safe

@admin.register(App)
class AppAdmin(admin.ModelAdmin):


    list_display = ("surname", "name", "otch", "phone",)
    list_filter = ("language", "edu_program",)
    search_fields = ("surname", "name", "otch",)
    # readonly_fields = ("admin_image", "admin_image2", "admin_image3",'admin_image4','admin_image5','admin_image6','admin_image7',)
    # fields = ("surname", "name", "otch", "phone", "edu_program", "language", "admin_image", "admin_image2", 'admin_image3','admin_image4','admin_image5','admin_image6','admin_image7',)

    def admin_image(self, obj):
        return mark_safe('<img src="%s"/ width="300" height="200">' % obj.id_card_front.url)

    admin_image.short_description = "Уд.лич лицевая"
    def admin_image2(self, obj):
        return mark_safe('<img src="%s"/ width="300" height="200">' % obj.id_card_back.url)

    admin_image2.short_description = "Уд.лич обратная"
    def admin_image3(self, obj):
        return mark_safe('<img src="%s"/ width="300" height="200">' % obj.diplom.url)

    admin_image3.short_description = "Диплом"

    def admin_image4(self, obj):
        return mark_safe('<img src="%s"/ width="300" height="200">' % obj.zayavka.url)

    admin_image4.short_description = "Заявление на обучение"

    def admin_image5(self, obj):
        return mark_safe('<img src="%s"/ width="300" height="200">' % obj.fluro.url)

    admin_image5.short_description = "075-у"

    def admin_image6(self, obj):
        return mark_safe('<img src="%s"/ width="300" height="200">' % obj.zdorovie.url)

    admin_image6.short_description = "063-у"

    def admin_image7(self, obj):
        return mark_safe('<img src="%s"/ width="300" height="200">' % obj.photo.url)

    admin_image7.short_description = "3x4 фото"

admin.site.register(EduProgram)