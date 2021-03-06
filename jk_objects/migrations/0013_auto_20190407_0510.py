# Generated by Django 2.2 on 2019-04-07 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jk_objects', '0012_jkobject_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='jkobject',
            name='contact_info',
            field=models.TextField(blank=True, null=True, verbose_name='Контактная информация'),
        ),
        migrations.AddField(
            model_name='jkobject',
            name='coordinates',
            field=models.CharField(blank=True, db_index=True, default=None, max_length=50, null=True, unique=True, verbose_name='Координаты'),
        ),
        migrations.AddField(
            model_name='jkobject',
            name='forma_1',
            field=models.URLField(blank=True, default=None, max_length=300, null=True, verbose_name='Форма 1'),
        ),
        migrations.AddField(
            model_name='jkobject',
            name='forma_2',
            field=models.URLField(blank=True, default=None, max_length=300, null=True, verbose_name='Форма 2'),
        ),
        migrations.AddField(
            model_name='jkobject',
            name='forma_3',
            field=models.URLField(blank=True, default=None, max_length=300, null=True, verbose_name='Форма 3'),
        ),
        migrations.AddField(
            model_name='jkobject',
            name='procent_info',
            field=models.TextField(blank=True, null=True, verbose_name='Коммисия'),
        ),
        migrations.AddField(
            model_name='jkobject',
            name='regulations_files_info',
            field=models.TextField(blank=True, null=True, verbose_name='Регламент и Файлы'),
        ),
        migrations.AddField(
            model_name='jkobject',
            name='site_develop',
            field=models.URLField(blank=True, default=None, max_length=300, null=True, verbose_name='Сайт застройщика'),
        ),
    ]
