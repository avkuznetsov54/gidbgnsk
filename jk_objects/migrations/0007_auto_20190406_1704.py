# Generated by Django 2.2 on 2019-04-06 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jk_objects', '0006_auto_20190406_1702'),
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
        migrations.AlterField(
            model_name='jkobject',
            name='district',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='district', to='jk_objects.District', verbose_name='Район'),
        ),
    ]
