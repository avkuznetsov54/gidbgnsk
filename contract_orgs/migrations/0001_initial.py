# Generated by Django 2.2 on 2019-04-08 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContractOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_1c', models.CharField(db_index=True, max_length=10, verbose_name='Номер 1С')),
                ('rooms', models.CharField(blank=True, max_length=10, verbose_name='Комнат')),
                ('street', models.CharField(blank=True, max_length=150, verbose_name='Улица')),
                ('num_house', models.CharField(blank=True, max_length=10, verbose_name='Номер дома')),
                ('district', models.CharField(blank=True, max_length=150, verbose_name='Район')),
                ('floor', models.CharField(blank=True, max_length=150, verbose_name='Этаж')),
                ('num_of_floors', models.CharField(blank=True, max_length=150, verbose_name='Этажность')),
                ('house_material', models.CharField(blank=True, max_length=150, verbose_name='Материал стен')),
                ('type_flat', models.CharField(blank=True, max_length=150, verbose_name='Тип квартиры')),
                ('all_square', models.FloatField(blank=True, db_index=True, verbose_name='Общая площадь')),
                ('living_square', models.FloatField(blank=True, db_index=True, verbose_name='Жилая площадь')),
                ('kitchen_square', models.FloatField(blank=True, db_index=True, verbose_name='Площадь кухни')),
                ('price', models.FloatField(blank=True, db_index=True, verbose_name='Стоимость')),
                ('num_flat', models.CharField(blank=True, max_length=10, verbose_name='Номер квартиры')),
                ('developer', models.CharField(blank=True, max_length=150, verbose_name='Застройщик')),
            ],
            options={
                'verbose_name': 'Подрядчик',
                'verbose_name_plural': 'Подрядчики',
                'ordering': ['number_1c'],
            },
        ),
    ]
