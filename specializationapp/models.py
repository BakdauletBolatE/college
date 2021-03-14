from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Specialization(models.Model):

    name = models.CharField('Название',max_length=255)
    uid = models.CharField('Код шифра',max_length=30)
    desctiption = models.TextField('Описание')
    photo = models.ImageField('Фото',upload_to='specialization/',blank=True,null=True)
    sertification = models.ImageField('Фото сертификата',upload_to='specializationC/',blank=True,null=True)
    duration = models.CharField('Продолжительность',max_length=30)

    def __str__(self):

        return self.name

    class Meta:

        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализаций'

class SpecializationFaq(models.Model):

    question = models.CharField('Вопрос', max_length=255)
    answer = models.TextField('Ответ')
    specialization = models.ForeignKey(Specialization,verbose_name='Специализация', related_name="faq", on_delete=models.CASCADE)

    def __str__(self):

        return self.question

    class Meta:

        verbose_name = 'Вопрос к специализаций'
        verbose_name_plural = 'Вопросы к специализаций'

class SpecializationComment(models.Model):

    text = models.TextField('Ответ')
    author = models.ForeignKey(User,verbose_name='Автор комента',on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specialization,verbose_name='Специализация', related_name='comments', on_delete=models.CASCADE)
    visible = models.BooleanField('Видимость коммента',default=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.text

    class Meta:

        verbose_name = 'Коментарий к специализацию'
        verbose_name_plural = 'Коментарий к специализаций'



