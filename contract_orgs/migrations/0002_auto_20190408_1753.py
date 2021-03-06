# Generated by Django 2.2 on 2019-04-08 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract_orgs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractorg',
            name='all_square',
            field=models.FloatField(blank=True, db_index=True, null=True, verbose_name='Общая площадь'),
        ),
        migrations.AlterField(
            model_name='contractorg',
            name='developer',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Застройщик'),
        ),
        migrations.AlterField(
            model_name='contractorg',
            name='district',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Район'),
        ),
        migrations.AlterField(
            model_name='contractorg',
            name='floor',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Этаж'),
        ),
        migrations.AlterField(
            model_name='contractorg',
            name='house_material',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Материал стен'),
        ),
        migrations.AlterField(
            model_name='contractorg',
            name='kitchen_square',
            field=models.FloatField(blank=True, db_index=True, null=True, verbose_name='Площадь кухни'),
        ),
        migrations.AlterField(
            model_name='contractorg',
            name='living_square',
            field=models.FloatField(blank=True, db_index=True, null=True, verbose_name='Жилая площадь'),
        ),
        migrations.AlterField(
            model_name='contractorg',
            name='num_flat',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Номер квартиры'),
        ),
        migrations.AlterField(
            model_name='contractorg',
            name='num_house',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Номер дома'),
        ),
        migrations.AlterField(
            model_name='contractorg',
            name='num_of_floors',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Этажность'),
        ),
        migrations.AlterField(
            model_name='contractorg',
            name='price',
            field=models.FloatField(blank=True, db_index=True, null=True, verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='contractorg',
            name='rooms',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Комнат'),
        ),
        migrations.AlterField(
            model_name='contractorg',
            name='street',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Улица'),
        ),
        migrations.AlterField(
            model_name='contractorg',
            name='type_flat',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Тип квартиры'),
        ),
    ]
