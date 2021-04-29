from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
import random

class PageCategory(models.Model):
    name = models.CharField('НАзвани катоегрий',max_length=255)
    linkto = models.CharField('Ссылка на чего либо',default=0,max_length=255,blank=True,null=True)
    order = models.IntegerField('Филтрация',default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self): # Тут мы создали новый метод
        return reverse('pageListView', args=[str(self.id)])
    class Meta:
        verbose_name = "Категория Страницы"
        verbose_name_plural = "Категорий Страницы"


class Page(models.Model):

    order = models.IntegerField('Филтрация',default=0)
    title = models.CharField('Название страницы',max_length=255)
    url = models.CharField('Ссылка НУЖНО ИМЯ',max_length=255)
    slug = models.SlugField('slug это обычный слаг',null=True,blank=True)
    link = models.CharField('Ссылку на сайт',null=True,blank=True,default=None,max_length=255)
    category = models.ForeignKey(PageCategory,related_name='page',on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

    def get_absolute_url(self): # Тут мы создали новый метод
        return reverse('pageDetailView', args=[str(self.id)])
    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"


class Widget(models.Model):

    widgettype = models.CharField(max_length=255)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,related_name="page")
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    page = models.ForeignKey(Page,on_delete=models.CASCADE,related_name="widgets")
    order = models.PositiveBigIntegerField(default=0)
    iic_id = models.CharField(max_length=255, null=True,blank=True)

    def get_absolute_update_url(self):
        return str(reverse('widgetUpdate', args=[str(self.id)]))

    def save(self, *args, **kwargs):
        randomIIC = f'#{self.id}' + ''.join([random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')) for x in range(12)])
        self.iic_id = randomIIC
        super().save(*args, **kwargs)  # Call the "real" save() method.
        

    def __str__(self):
        return str(self.id)


class WidgetText(models.Model):

    title = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True)

    def get_absolute_update_url(self):
        return str(reverse('widgetTextUpdate', args=[str(self.id)]))

class WidgetOnlyText(models.Model):

    title = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True)

    def get_absolute_update_url(self):
        return str(reverse('widgetOnlyTextUpdate', args=[str(self.id)]))

class WidgetPhoto(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to="Images/",blank=True,null=True)

    def get_absolute_update_url(self):
        return str(reverse('widgetPhotoUpdate', args=[str(self.id)]))

class WidgetGalery(models.Model):

    title = models.CharField(max_length=255,blank=True,null=True)


class WidgetGalleryPhotos(models.Model):

    image = models.ImageField(upload_to="Images/",blank=True,null=True)
    widgetGalery = models.ForeignKey(WidgetGalery,on_delete=models.CASCADE ,related_name="images")