from django.db import models


# Create your models here.


class District(models.Model):
    """Модель Района"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Район')
    subname = models.CharField(max_length=150, unique=True, blank=True, verbose_name='Сокращённое')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'
        ordering = ['name']


class DeadlineBuilding(models.Model):
    """Модель Срок сдачи"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Срок сдачи')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Срок сдачи'
        verbose_name_plural = 'Сроки сдачи'
        # ordering = ['name']


class Developer(models.Model):
    """Модель Застройщик"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Застройщик')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Застройщик'
        verbose_name_plural = 'Застройщики'
        ordering = ['name']


class HouseMaterial(models.Model):
    """Модель Материал дома"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Материал дома')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Материал дома'
        verbose_name_plural = 'Материалы дома'
        ordering = ['name']


class PaymentМethod(models.Model):
    """Модель Способ оплаты"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Способ оплаты')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Способ оплаты'
        verbose_name_plural = 'Способы оплаты'
        ordering = ['name']


class Bank(models.Model):
    """Модель Банк"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Банк')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Банк'
        verbose_name_plural = 'Банки'
        ordering = ['name']


class ClassBuilding(models.Model):
    """Модель Класс Жилья"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Класс Жилья')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Класс Жилья'
        verbose_name_plural = 'Классы Жилья'
        ordering = ['name']


class FinishingFlat(models.Model):
    """Модель Отделка Жилья"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Отделка квартиры')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отделка квартиры'
        verbose_name_plural = 'Отделки квартиры'
        ordering = ['name']


class JkObject(models.Model):
    """Модель Жилого Комплекса"""
    name = models.CharField(max_length=150, db_index=True, unique=True, verbose_name='Жилой Комплекс')
    developer = models.ForeignKey(Developer,
                                  on_delete=models.SET_DEFAULT,
                                  verbose_name='Застройщик',
                                  related_name="developer",
                                  default=None,
                                  null=True,
                                  blank=True)
    district = models.ForeignKey(District,
                                 on_delete=models.SET_DEFAULT,
                                 verbose_name='Район',
                                 related_name='district',
                                 default=None,
                                 null=True,
                                 blank=True)
    address = models.CharField(max_length=150, db_index=True, unique=True, verbose_name='Адрес',
                               default=None,
                               null=True, blank=True)
    class_building = models.ForeignKey(ClassBuilding,
                                       on_delete=models.SET_DEFAULT,
                                       verbose_name='Класс Жилья',
                                       related_name='class_building',
                                       default=None,
                                       null=True,
                                       blank=True)

    forma_1 = models.CharField(max_length=300, verbose_name='Форма 1',
                               default=None,
                               null=True, blank=True)
    forma_2 = models.CharField(max_length=300, verbose_name='Форма 2',
                               default=None,
                               null=True, blank=True)
    forma_3 = models.URLField(max_length=300, verbose_name='Форма 3',
                              default=None,
                              null=True, blank=True)

    contact_info = models.TextField(blank=True, null=True, verbose_name='Контактная информация')
    regulations_files_info = models.TextField(blank=True, null=True, verbose_name='Регламент и Файлы')
    procent_info = models.TextField(blank=True, null=True, verbose_name='Коммисия')
    site_develop = models.URLField(max_length=300, verbose_name='Сайт застройщика',
                                   default=None,
                                   null=True, blank=True)
    coordinates = models.CharField(max_length=50, db_index=True, unique=True, verbose_name='Координаты',
                                   default=None,
                                   null=True, blank=True)

    image = models.ImageField(upload_to='jkobject_images/', blank=True)

    is_active = models.BooleanField(default=True, verbose_name='Показывать')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жилой Комплекс'
        verbose_name_plural = 'Жилые Комплексы'
        ordering = ['name']


class HouseOfObject(models.Model):
    """Модель Дома Объекта"""
    jk_object = models.ForeignKey(JkObject, on_delete=models.CASCADE,
                                  verbose_name='Жилой комплекс',
                                  related_name="jkobject",
                                  default=None,
                                  null=True,
                                  blank=True)

    address = models.CharField(max_length=150, db_index=True, unique=True, verbose_name='Адрес', blank=True)

    deadline = models.ForeignKey(DeadlineBuilding,
                                 on_delete=models.SET_DEFAULT,
                                 verbose_name='Срок сдачи',
                                 related_name='deadline',
                                 default=None,
                                 null=True,
                                 blank=True)

    floors = models.CharField(max_length=30, db_index=True, verbose_name='Этажность', blank=True)

    house_material = models.ForeignKey(HouseMaterial,
                                       on_delete=models.SET_DEFAULT,
                                       verbose_name='Материал дома',
                                       related_name='housematerial',
                                       default=None,
                                       null=True,
                                       blank=True)

    finishing_flat = models.ManyToManyField(FinishingFlat,
                                            verbose_name='Отделка квартиры',
                                            related_name='finishingflat',
                                            default=None,
                                            null=True,
                                            blank=True)

    payment_method = models.ManyToManyField(PaymentМethod,
                                            verbose_name='Способы оплаты',
                                            related_name='paymentmethod',
                                            default=None,
                                            null=True,
                                            blank=True)

    banks = models.ManyToManyField(Bank,
                                   verbose_name='Банки',
                                   related_name='bank',
                                   default=None,
                                   null=True,
                                   blank=True)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Дом объекта'
        verbose_name_plural = 'Дома объекта'
        ordering = ['address']
