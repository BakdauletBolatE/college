from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):

    name = models.CharField('Курс',max_length=255)

    def __str__(self):

        return self.name


class Cemester(models.Model):

    name = models.CharField('Семестр',max_length=255)

    def __str__(self):

        return self.name

class Weekend(models.Model):

    name = models.CharField('Неделя',max_length=255)

    def __str__(self):

        return self.name



class Group(models.Model):

    name = models.CharField('Имя группы',max_length=255)
    course = models.ForeignKey(Course,verbose_name='Курс',on_delete=models.CASCADE)

    def __str__(self):

        return self.name


class Subject(models.Model):

    name = name = models.CharField('Имя предмета',max_length=255)

    def __str__(self):

        return self.name

class TeacherProfile(models.Model):

    user = models.OneToOneField(User,verbose_name='Аккаунт',related_name='teacher',on_delete=models.CASCADE)
    groups = models.ManyToManyField(Group,verbose_name='Группы учителей',related_name='teacherpro')
    subject = models.ManyToManyField(Subject,verbose_name='Предмет',related_name='teacher')

    def __str__(self):

        return self.user.username




class Tasks(models.Model):

    question = models.CharField('Имя заданий',max_length=255)
    files = models.FileField('Файлы',upload_to='Files/')
    group = models.ForeignKey(Group,verbose_name='Заданий для группы',related_name='task',on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,verbose_name='Предмет',related_name='task',on_delete=models.CASCADE)
    cemester = models.ForeignKey(Cemester,on_delete=models.CASCADE,verbose_name='Семестр для группы',related_name='task')
    week = models.ForeignKey(Weekend,on_delete=models.CASCADE,verbose_name='Неделя для группы',related_name='task')
    user = models.ForeignKey(User,verbose_name='Аккаунт',related_name='task',on_delete=models.CASCADE)

    def __str__(self):

        return self.question


class StuudentProfile(models.Model):

    user = models.OneToOneField(User,verbose_name='Аккаунт',related_name='student',on_delete=models.CASCADE)
    group = models.ForeignKey(Group,verbose_name='Группа студента',related_name='student',on_delete=models.CASCADE)
    subject = models.ManyToManyField(Subject,verbose_name='Предметы',related_name='student')

    def __str__(self):

        return self.user.username


class Answer(models.Model):

    name = models.CharField('Имя заданий',max_length=255)
    files = models.FileField('Файлы',upload_to='Files/')
    task = models.ForeignKey(Tasks,verbose_name='Задания',on_delete=models.CASCADE,related_name='answers')
    user = models.ForeignKey(User,verbose_name='Аккаунт',related_name='answer',on_delete=models.CASCADE)

    def __str__(self):

        return self.name


class Rating(models.Model):

    rate = models.IntegerField('Рейтинг')
    answer = models.OneToOneField(Answer,on_delete=models.CASCADE,related_name='rate')

    def __str__(self):

        return self.rate