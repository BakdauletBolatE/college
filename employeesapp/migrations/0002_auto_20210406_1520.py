# Generated by Django 3.1.7 on 2021-04-06 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeesapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='employees',
            name='name_kk',
            field=models.CharField(max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='employees',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='employees',
            name='position_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='employees',
            name='position_kk',
            field=models.CharField(max_length=255, null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='employees',
            name='position_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='government',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='government',
            name='name_kk',
            field=models.CharField(max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='government',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='government',
            name='position_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='government',
            name='position_kk',
            field=models.CharField(max_length=255, null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='government',
            name='position_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Должность'),
        ),
    ]