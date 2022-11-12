from django.db import models
from specializationapp.models import Specialization, Qualification
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
# Create your models here.
from ckeditor.fields import RichTextField


class Government(models.Model):
    name = models.CharField('Имя', max_length=255)
    age = models.IntegerField('Возраст')
    position = models.CharField('Должность', max_length=255)
    isimp = models.BooleanField('Важность')
    about = RichTextField('Описание', default="Пишите описание")
    photo = models.ImageField('Фото', upload_to='government/')
    order = models.IntegerField('Филтрация')

    def get_absolute_url(self):
        return reverse('empapp:gDetailView', kwargs={'pk': self.id})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Руководство колледжа'
        verbose_name_plural = 'Руководство колледжа'


class Employees(models.Model):
    name = models.CharField('Имя', max_length=255)
    age = models.IntegerField('Возраст')
    specialization = models.ForeignKey(Specialization, verbose_name='Специализация', related_name="employees",
                                       blank=True, null=True, on_delete=models.CASCADE)
    qualification = models.ForeignKey(Qualification, verbose_name='Квалификация', related_name="employees", blank=True,
                                      null=True, on_delete=models.CASCADE)
    about = RichTextField('Описание', default="Пишите описание")
    position = models.CharField('Должность', max_length=255)
    photo = models.ImageField('Фото', upload_to='employees/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('empapp:tDetailView', kwargs={'pk': self.id})

    class Meta:
        verbose_name = 'Преподаватель колледжа'
        verbose_name_plural = 'Преподаватели колледжа'


class Leсture(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    video_link = models.CharField(max_length=255, blank=True, null=True)
    video = models.CharField(max_length=255, null=True, blank=True)

    teacher = models.ForeignKey(Employees, null=True, blank=True, on_delete=models.CASCADE, related_name='lectures')

    class Meta:
        verbose_name = 'Лекция'
        verbose_name_plural = 'Лекций'


class EmployeesLikes(models.Model):
    employees = models.ForeignKey(Employees,
                                  verbose_name='Сотрудник которому должен нажаться лайк',
                                  on_delete=models.CASCADE)
    likeuser = models.ForeignKey(User,
                                 verbose_name='Пользователь который нажал(а) лайк',
                                 on_delete=models.CASCADE)
    is_check = models.BooleanField('Чек', default=False)
    created_at = models.DateTimeField('Когда создано', default=timezone.now)

    def __str__(self):
        return ''

    class Meta:
        verbose_name = 'Лайк к преподавателю'
        verbose_name_plural = 'Лайки к преподавателю'
