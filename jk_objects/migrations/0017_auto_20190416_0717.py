# Generated by Django 2.2 on 2019-04-16 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jk_objects', '0016_jkobject_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jkobject',
            name='forma_1',
            field=models.CharField(blank=True, default=None, max_length=300, null=True, verbose_name='Форма 1'),
        ),
        migrations.AlterField(
            model_name='jkobject',
            name='forma_2',
            field=models.CharField(blank=True, default=None, max_length=300, null=True, verbose_name='Форма 2'),
        ),
    ]
