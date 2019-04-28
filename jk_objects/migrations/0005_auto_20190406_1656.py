# Generated by Django 2.2 on 2019-04-06 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jk_objects', '0004_auto_20190406_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jkobject',
            name='class_building',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='class_building', to='jk_objects.ClassBuilding', verbose_name='Класс Жилья'),
        ),
        migrations.AlterField(
            model_name='jkobject',
            name='developer',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='developer', to='jk_objects.Developer', verbose_name='Застройщик'),
        ),
    ]