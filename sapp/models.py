from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Abiturent(models.Model):

    title = models.CharField(max_length=255)
    description = RichTextUploadingField()
    background = models.ImageField(upload_to='Background/')

class Files(models.Model):

    abiturent = models.ForeignKey(Abiturent, on_delete=models.CASCADE, related_name='files')
    fileName = models.CharField(max_length=255)
    file = models.FileField(upload_to='Files/')

class Appeal(models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
