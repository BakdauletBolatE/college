from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Section(models.Model):

    name = models.CharField('Название',max_length=255)
    uid = models.CharField('Код шифра',max_length=30)

    class Meta:

        verbose_name = '01 Профиль'
        verbose_name_plural = '01 Профили'

    def __str__(self):

        return self.uid + " " + self.name




class SubSection(models.Model):

    name = models.CharField('Название',max_length=255)
    uid = models.CharField('Код шифра',max_length=30)
    section = models.ForeignKey(Section,related_name="subsection",verbose_name="Профиль",on_delete=models.CASCADE)

    class Meta:

        verbose_name = '02 Подпрофиль'
        verbose_name_plural = '02 Подпрофили'

    def __str__(self):

        return self.uid + " " + self.name




class Specialization(models.Model):

    name = models.CharField('Название',max_length=255)
    uid = models.CharField('Код шифра',max_length=30)
    desctiption = models.TextField('Описание')
    photo = models.ImageField('Фото',upload_to='specialization/',blank=True,null=True)
    sertification = models.ImageField('Фото сертификата',upload_to='specializationC/',blank=True,null=True)
    duration = models.CharField('Продолжительность',max_length=30)
    subsection = models.ForeignKey(SubSection,related_name="specialization",verbose_name="подпроифиль",on_delete=models.CASCADE)

    def __str__(self):

        return self.uid + " " + self.name

    class Meta:

        verbose_name = '03 Специализация'
        verbose_name_plural = '03 Специализаций'

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


class Qualification(models.Model):

    name = models.CharField('Название',max_length=255)
    uid = models.CharField('Код шифра',max_length=30)
    specialization = models.ForeignKey(Specialization,related_name="Qualification",verbose_name="Специялизация",on_delete=models.CASCADE)

    def __str__(self):

        return self.uid + " " + self.name

    class Meta:

        verbose_name = '04 Квалификация'
        verbose_name_plural = '04 Квалификаций'