# Generated by Django 3.1.7 on 2021-04-29 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, verbose_name='Филтрация')),
                ('title', models.CharField(max_length=255, verbose_name='Название страницы')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Название страницы')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='Название страницы')),
                ('title_kk', models.CharField(max_length=255, null=True, verbose_name='Название страницы')),
                ('url', models.CharField(max_length=255, verbose_name='Ссылка НУЖНО ИМЯ')),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='slug это обычный слаг')),
                ('link', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Ссылку на сайт')),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
            },
        ),
        migrations.CreateModel(
            name='PageCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='НАзвани катоегрий')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='НАзвани катоегрий')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='НАзвани катоегрий')),
                ('name_kk', models.CharField(max_length=255, null=True, verbose_name='НАзвани катоегрий')),
                ('linkto', models.CharField(blank=True, default=0, max_length=255, null=True, verbose_name='Ссылка на чего либо')),
                ('order', models.IntegerField(default=0, verbose_name='Филтрация')),
            ],
            options={
                'verbose_name': 'Категория Страницы',
                'verbose_name_plural': 'Категорий Страницы',
            },
        ),
        migrations.CreateModel(
            name='WidgetGalery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WidgetOnlyText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('description_ru', models.TextField(blank=True, null=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('description_kk', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WidgetPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('title_ru', models.CharField(blank=True, max_length=255, null=True)),
                ('title_en', models.CharField(blank=True, max_length=255, null=True)),
                ('title_kk', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('description_ru', models.TextField(blank=True, null=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('description_kk', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Images/')),
            ],
        ),
        migrations.CreateModel(
            name='WidgetText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('title_ru', models.CharField(blank=True, max_length=255, null=True)),
                ('title_en', models.CharField(blank=True, max_length=255, null=True)),
                ('title_kk', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('description_ru', models.TextField(blank=True, null=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('description_kk', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WidgetGalleryPhotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Images/')),
                ('widgetGalery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='page.widgetgalery')),
            ],
        ),
        migrations.CreateModel(
            name='Widget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('widgettype', models.CharField(max_length=255)),
                ('object_id', models.PositiveIntegerField()),
                ('order', models.PositiveBigIntegerField(default=0)),
                ('iic_id', models.CharField(blank=True, max_length=255, null=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page', to='contenttypes.contenttype')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='widgets', to='page.page')),
            ],
        ),
        migrations.AddField(
            model_name='page',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page', to='page.pagecategory'),
        ),
    ]
