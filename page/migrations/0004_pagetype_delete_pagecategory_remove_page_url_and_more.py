# Generated by Django 4.1.3 on 2022-12-08 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0005_rename_check_newslikes_is_check'),
        ('page', '0003_remove_widget_content_type_remove_widget_page_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Тип страницы',
                'verbose_name_plural': 'Типы страниц',
            },
        ),
        migrations.DeleteModel(
            name='PageCategory',
        ),
        migrations.RemoveField(
            model_name='page',
            name='url',
        ),
        migrations.AddField(
            model_name='page',
            name='content',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='newsapp.newspost'),
        ),
        migrations.AddField(
            model_name='page',
            name='page_type',
            field=models.ForeignKey(blank=True, default=1, max_length=255, null=True, on_delete=django.db.models.deletion.CASCADE, to='page.pagetype'),
        ),
    ]