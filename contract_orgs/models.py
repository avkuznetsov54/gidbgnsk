from django.db import models


class ContractOrg(models.Model):
    """Модель Подрядчик"""
    number_1c = models.CharField(max_length=10, db_index=True, verbose_name='Номер 1С')
    rooms = models.CharField(max_length=10, null=True, blank=True, verbose_name='Комнат')
    street = models.CharField(max_length=150, null=True, blank=True, verbose_name='Улица')
    num_house = models.CharField(max_length=10, null=True, blank=True, verbose_name='Номер дома')
    district = models.CharField(max_length=150, null=True, blank=True, verbose_name='Район')
    floor = models.CharField(max_length=150, null=True, blank=True, verbose_name='Этаж')
    num_of_floors = models.CharField(max_length=150, null=True, blank=True, verbose_name='Этажность')
    house_material = models.CharField(max_length=150, null=True, blank=True, verbose_name='Материал стен')
    type_flat = models.CharField(max_length=150, null=True, blank=True, verbose_name='Тип квартиры')
    all_square = models.FloatField(db_index=True, null=True, blank=True, verbose_name='Общая площадь')
    living_square = models.FloatField(db_index=True, null=True, blank=True, verbose_name='Жилая площадь')
    kitchen_square = models.FloatField(db_index=True, null=True, blank=True, verbose_name='Площадь кухни')
    price = models.FloatField(db_index=True, blank=True, null=True, verbose_name='Стоимость')
    num_flat = models.CharField(max_length=10, blank=True, null=True, verbose_name='Номер квартиры')
    developer = models.CharField(max_length=150, blank=True, null=True, verbose_name='Застройщик')

    def __str__(self):
        return self.number_1c

    class Meta:
        verbose_name = 'Подрядчик'
        verbose_name_plural = 'Подрядчики'
        ordering = ['number_1c']
