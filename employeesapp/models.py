from django.db import models
from specializationapp.models import Specialization
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Government(models.Model):

    name = models.CharField('Имя',max_length=255)
    age = models.IntegerField('Возраст')
    position = models.CharField('Должность',max_length=255)
    isimp = models.BooleanField('Важность')
    photo = models.ImageField('Фото',upload_to='government/')
    order = models.IntegerField('Филтрация')

    def __str__(self):

        return self.name

    class Meta:

        verbose_name = 'Руководство колледжа'
        verbose_name_plural = 'Руководство колледжа'

class Employees(models.Model):

    name = models.CharField('Имя',max_length=255)
    age = models.IntegerField('Возраст')
    specialization = models.ForeignKey(Specialization,verbose_name='Специализация',related_name="employees", blank=True,null=True,on_delete=models.CASCADE)
    position = models.CharField('Должность',max_length=255)
    photo = models.ImageField('Фото',upload_to='employees/')

    def __str__(self):

        return self.name

    class Meta:

        verbose_name = 'Преподаватель колледжа'
        verbose_name_plural = 'Преподаватели колледжа'


class EmployeesLikes(models.Model):

    employees = models.ForeignKey(Employees,
                                verbose_name='Сотрудник которому должен нажаться лайк',
                                on_delete=models.CASCADE)
    likeuser = models.ForeignKey(User,
                                verbose_name='Пользователь который нажал(а) лайк',
                                on_delete=models.CASCADE)
    check = models.BooleanField('Чек',default=False)
    created_at = models.DateTimeField('Когда создано',default=timezone.now)

    def __str__(self):

        return f'к сотруднику {self.employees.name} нажал(а) лайк пользователь{self.likeuser.username}'
    
    class Meta:

        verbose_name = 'Лайк к преподавателю'
        verbose_name_plural = 'Лайки к преподавателю'