from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from newsapp.models import NewsPost


class PageType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип страницы"
        verbose_name_plural = "Типы страниц"


class Page(models.Model):
    order = models.IntegerField('Филтрация', default=0)
    title = models.CharField('Название страницы', max_length=255)
    slug = models.SlugField('slug это обычный слаг', null=True, blank=True)
    link = models.CharField('Ссылка на страницу', null=True, blank=True, default=None, max_length=255)
    content = models.ForeignKey(NewsPost, null=True, blank=True, on_delete=models.DO_NOTHING)
    page_type = models.ForeignKey(PageType, max_length=255, null=True, blank=True, default=1, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # Тут мы создали новый метод
        return reverse('pageDetailView', args=[str(self.id)])

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"
