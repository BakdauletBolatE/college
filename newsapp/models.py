from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class NewsCategory(models.Model):

    name = models.CharField('Название категорий',max_length=255)
    created_at = models.DateTimeField('Когда создано',default=timezone.now)

    def __str__(self):

        return self.name

    class Meta:

        verbose_name = 'Категория новости'
        verbose_name_plural = 'Категорий новости'

class NewsPost(models.Model):
    title = models.CharField('Загаловок поста',max_length=255)
    description = models.TextField('Описание поста')
    category = models.ForeignKey(NewsCategory,verbose_name='Категория новости',default=0,on_delete=models.CASCADE)
    created_at = models.DateTimeField('Когда создано',default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:

        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

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
