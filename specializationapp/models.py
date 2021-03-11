from django.db import models

# Create your models here.

class Specialization(models.Model):

    name = models.CharField('Название',max_length=255)
    uid = models.CharField('Код шифра',max_length=30)
    desctiption = models.TextField('Описание')
    photo = models.ImageField('Фото',upload_to='specialization/',blank=True,null=True)

    def __str__(self):

        return self.name
