# Generated by Django 2.2 on 2019-04-09 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jk_objects', '0015_auto_20190408_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='jkobject',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Показывать'),
        ),
    ]