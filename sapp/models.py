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
