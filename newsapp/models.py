from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class NewsCategory(models.Model):

    name = models.CharField('Название категорий',max_length=255)
    poster = models.ImageField('Постер',upload_to="newsC/")
    created_at = models.DateTimeField('Когда создано',default=timezone.now)

    def __str__(self):

        return self.name

    class Meta:

        verbose_name = 'Категория новости'
        verbose_name_plural = 'Категорий новости'

class NewsPost(models.Model):
    title = models.CharField('Загаловок поста',max_length=255)
    description = models.TextField('Описание поста')
    poster = models.ImageField('Постер',upload_to="news/")
    category = models.ForeignKey(NewsCategory,verbose_name='Категория новости',default=0,on_delete=models.CASCADE)
    created_at = models.DateTimeField('Когда создано',default=timezone.now)

    def __str__(self):
        return self.title_ru

    class Meta:

        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class GalleryPost(models.Model):
    title = models.CharField('Названия',max_length=255,null=True,blank=True)
    url = models.CharField('Ссылка на ютуб',max_length=255,null=True,blank=True)
    poster = models.ImageField('Постер',upload_to="gallery/",null=True,blank=True)
    created_at = models.DateTimeField('Когда создано',default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:

        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'

class NewsLikes(models.Model):

    newspost = models.ForeignKey(NewsPost,
                                verbose_name='Пост которому должен нажаться лайк',
                                on_delete=models.CASCADE)
    likeuser = models.ForeignKey(User,
                                verbose_name='Пользователь который нажал(а) лайк',
                                on_delete=models.CASCADE)
    check = models.BooleanField('Чек',default=False)
    created_at = models.DateTimeField('Когда создано',default=timezone.now)

    def __str__(self):

        return f'к посту {self.newspost.title} нажал(а) лайк пользователь{self.likeuser.username}'

    class Meta:

        verbose_name = 'Лайк к новостью'
        verbose_name_plural = 'Лайки к новостью'

class NewsComment(models.Model):

    text = models.TextField('Ответ')
    author = models.ForeignKey(User,verbose_name='Автор комента',on_delete=models.CASCADE)
    specialization = models.ForeignKey(NewsPost,verbose_name='Новость', related_name='comments', on_delete=models.CASCADE)
    visible = models.BooleanField('Видимость коммента',default=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.text

    class Meta:

        verbose_name = 'Коментарий к новостью'
        verbose_name_plural = 'Коментарий к новостью'
