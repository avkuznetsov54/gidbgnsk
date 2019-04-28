from django.db import models
from django.utils import timezone

from jk_objects.models import JkObject


# class SignerAndPosition(models.Model):
#     """Модель подписант и должность"""
#     name = models.CharField(max_length=150, unique=True, verbose_name='ФИО подписанта в реквизитах')
#     s_p_header = models.CharField(max_length=150, blank=False, verbose_name='В шапке')
#     position = models.CharField(max_length=150, blank=True, verbose_name='Должность')
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Подписант'
#         verbose_name_plural = 'Подписанты'
#         ordering = ['name']


class AdditionalValue(models.Model):
    """Модель Дополнительные Значения"""
    name = models.CharField(max_length=200, unique=True, verbose_name='Имя')
    description = models.CharField(max_length=200, unique=True, verbose_name='Описание')
    value = models.TextField(blank=True, verbose_name='Значение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Доп. значение'
        verbose_name_plural = 'Доп. значения'


class Office(models.Model):
    """Модель Офис - РОП - email РОПа"""
    office = models.CharField(max_length=150, unique=True, verbose_name='Офис')
    name_rop = models.CharField(max_length=150, blank=True, verbose_name='ФИО РОПа')
    email = models.EmailField(blank=True, verbose_name='Email РОПа')

    def __str__(self):
        return self.office

    class Meta:
        verbose_name = 'Офис/РОП/email'
        verbose_name_plural = 'Офисы/РОПы/emails'
        ordering = ['office']


# ф-ция генерит название папки для шаблона уведомления
def generate_filename(self, filename):
    url = "notice_forms/templates_notices/%s/%s" % (self.nick_name, filename)
    return url


class NoticeTemplate(models.Model):
    """Модель шаблона уведомления"""
    nick_name = models.CharField(max_length=150, unique=True, verbose_name='Название уведомления',
                                 help_text="Используйте латинские буквы.<br>Пример: yasniy_bereg_form_1")

    jk_object = models.CharField(max_length=150, blank=True, verbose_name='Жилой комплекс',
                                 help_text="Впишите название жилого комплекса")

    emails_developer = models.CharField(max_length=200, verbose_name='Email(s) застройщика',
                                        help_text="1) Сперва для проверки впишите тестовую почту, после тестирования измените на почту застройщика.<br>2) Если у застройщика больше чем одна почта, то напишите почты через запятую без пробелов.")

    # файл с шаблоном уведомления
    file_template = models.FileField(upload_to=generate_filename, verbose_name='Файл шаблона уведомления',
                                     help_text="Выберите подготовленный файл, для генерации уведомления.<br>Используйте .docx формат.")

    # файл пустого уведомления
    file_null_notice = models.FileField(upload_to=generate_filename, verbose_name='Файл пустого уведомления',
                                        help_text='Укажите файл пустого уведомления, будет скачиваться при нажатию на кнопку "Скачать пустое".<br>Используйте .docx формат.')

    # Определение принадлежности

    type_for_lawyer_is_active = models.BooleanField(default=False,
                                                    verbose_name='Отправлять ипотечному специалисту или нет (наличные/ипотека)',
                                                    help_text='Если есть необходимость отправлять копию ипотечному специалисту.<br>Внесите email специалиста в разделе "Настройка уведомлений" -> "Доп. значения".')

    TYPE_NOTICE_CHOICES = (
        ('uvedd', 'Уведомление'),
        ('bronn', 'Бронирование'),
        ('uvedd_bronn', 'Уведомление или Бронирование')
    )
    type_for_notice_choice = models.CharField(choices=TYPE_NOTICE_CHOICES, max_length=50, blank=True,
                                              verbose_name='Уведомление или бронирование',
                                              help_text='Определяет тип уведомления.<br>Если выбрать пункт "Уведомление или Бронирование", то нужно будет указать тип при заполнении формы пользователем.')

    # Обязательные поля для вывода в форму
    office_is_active = models.BooleanField(default=True, verbose_name='Выбор офиса',
                                           help_text='Если нужен выбор офиса, занесите сначало офисы в "Настройка уведомлений" -> "Офисы/РОПы/emails".<br>Если включить выбор офиса станет обязателен.')

    fio_client = models.CharField(max_length=150, blank=True, verbose_name='ФИО клиента', default='fioclientform')
    fio_client_is_active = models.BooleanField(default=True, verbose_name='ФИО клиента')

    phone_client = models.CharField(max_length=150, blank=True, verbose_name='Телефон клиента',
                                    default='phoneclientform')
    phone_client_is_active = models.BooleanField(default=True, verbose_name='Телефон клиента')

    fio_agent = models.CharField(max_length=150, blank=True, verbose_name='ФИО агента', default='fioagentform')
    fio_agent_is_active = models.BooleanField(default=True, verbose_name='ФИО агента')

    phone_agent = models.CharField(max_length=150, blank=True, verbose_name='Телефон агента', default='phoneagentform')
    phone_agent_is_active = models.BooleanField(default=True, verbose_name='Телефон агента')

    email_agent = models.CharField(max_length=50, blank=True, verbose_name='Email агента', default='emailagentform')
    email_agent_is_active = models.BooleanField(default=True, verbose_name='Email агента')

    # Необязательные поля для вывода в форме
    sum_of_rooms = models.CharField(max_length=20, blank=True, verbose_name='Кол-во комнат', default='sumofroomsform')
    sum_of_rooms_is_active = models.BooleanField(default=False, verbose_name='Кол-во комнат')

    apartment_number = models.CharField(max_length=20, blank=True, verbose_name='Номер квартиры',
                                        default='apartmentnumberform')
    apartment_number_is_active = models.BooleanField(default=False, verbose_name='Номер квартиры')

    floor = models.CharField(max_length=20, blank=True, verbose_name='Этаж', default='floorform')
    floor_is_active = models.BooleanField(default=False, verbose_name='Этаж')

    square = models.CharField(max_length=20, blank=True, verbose_name='Площадь квартиры', default='squareform')
    square_is_active = models.BooleanField(default=False, verbose_name='Площадь квартиры')

    address_object = models.CharField(max_length=150, blank=True, verbose_name='Адрес дома',
                                      default='addressobjectform')
    address_object_is_active = models.BooleanField(default=False, verbose_name='Адрес дома')

    number_object = models.CharField(max_length=20, blank=True, verbose_name='Номер дома', default='numberobjectform')
    number_object_is_active = models.BooleanField(default=False, verbose_name='Номер дома')

    section_object = models.CharField(max_length=20, blank=True, verbose_name='Секция', default='sectionobjectform')
    section_object_is_active = models.BooleanField(default=False, verbose_name='Секция')

    price = models.CharField(max_length=20, blank=True, verbose_name='Стоимость квартиры', default='priceform')
    price_is_active = models.BooleanField(default=False, verbose_name='Стоимость квартиры')

    price_m = models.CharField(max_length=20, blank=True, verbose_name='Стоимость за 1 кв.м.', default='pricemform')
    price_m_is_active = models.BooleanField(default=False, verbose_name='Стоимость за 1 кв.м.')

    client_passport_details = models.CharField(max_length=200, blank=True, verbose_name='Паспортные данные клиента',
                                               default='clientpassportdetailsform')
    client_passport_details_is_active = models.BooleanField(default=False,
                                                            verbose_name='Паспортные данные клиента')

    place_of_residence = models.CharField(max_length=200, blank=True, verbose_name='Адрес прописки',
                                          default='placeofresidenceform')
    place_of_residence_is_active = models.BooleanField(default=False, verbose_name='Адрес прописки')

    form_of_payment = models.CharField(max_length=150, blank=True, verbose_name='Форма расчёта',
                                       default='formofpaymentform')
    form_of_payment_is_active = models.BooleanField(default=False, verbose_name='Форма расчёта')

    consult_date = models.CharField(max_length=20, blank=True, verbose_name='Дата консультации',
                                    default='consultdateform')
    consult_date_is_active = models.BooleanField(default=False, verbose_name='Дата консультации')

    consult_time = models.CharField(max_length=20, blank=True, verbose_name='Время консультации',
                                    default='consulttimeform')
    consult_time_is_active = models.BooleanField(default=False, verbose_name='Время консультации')

    manager_select = models.CharField(max_length=150, blank=True, verbose_name='Выбор менеджера',
                                      default='managerselectform')
    manager_select_is_active = models.BooleanField(default=False, verbose_name='Выбор менеджера')

    # Дополнительные значени
    add_value_1 = models.CharField(max_length=150, blank=True, verbose_name='Доп. значение 1')
    add_value_1_is_active = models.BooleanField(default=False, verbose_name='Доп. значение 1')

    add_value_2 = models.CharField(max_length=150, blank=True, verbose_name='Доп. значение 2')
    add_value_2_is_active = models.BooleanField(default=False, verbose_name='Доп. значение 2')

    add_value_3 = models.CharField(max_length=150, blank=True, verbose_name='Доп. значение 3')
    add_value_3_is_active = models.BooleanField(default=False, verbose_name='Доп. значение 3')

    add_value_4 = models.CharField(max_length=150, blank=True, verbose_name='Доп. значение 4')
    add_value_4_is_active = models.BooleanField(default=False, verbose_name='Доп. значение 4')

    add_value_5 = models.CharField(max_length=150, blank=True, verbose_name='Доп. значение 5')
    add_value_5_is_active = models.BooleanField(default=False, verbose_name='Доп. значение 5')

    def __str__(self):
        return self.nick_name

    class Meta:
        verbose_name = 'Шаблон уведомления'
        verbose_name_plural = 'Шаблоны уведомлений'
        ordering = ['nick_name']


class Notice(models.Model):
    """Модель полей уведомления"""
    date_time_send = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')
    developer = models.CharField(max_length=150, blank=True, verbose_name='Застройщик')
    jk_object = models.CharField(max_length=150, blank=True, verbose_name='Жилой комплекс')
    emails_developer = models.CharField(max_length=200, blank=True, null=True, verbose_name='Email(s) застройщика')

    type_for_lawyer = models.CharField(max_length=20, blank=True,
                                       verbose_name='Отправлять юристу или нет (наличные/ипотека)')
    type_for_notice = models.CharField(max_length=20, blank=True, verbose_name='Уведомление или бронирование')

    office = models.CharField(max_length=150, blank=True, null=True, verbose_name='Офис')
    fio_client = models.CharField(max_length=150, blank=True, verbose_name='ФИО клиента')
    phone_client = models.CharField(max_length=150, blank=True, verbose_name='Телефон клиента')
    fio_agent = models.CharField(max_length=150, blank=True, verbose_name='ФИО агента')
    phone_agent = models.CharField(max_length=150, blank=True, verbose_name='Телефон агента')
    email_agent = models.CharField(max_length=50, blank=True, verbose_name='Email агента')

    sum_of_rooms = models.CharField(max_length=20, blank=True, verbose_name='Кол-во комнат')
    apartment_number = models.CharField(max_length=20, blank=True, verbose_name='Номер квартиры')
    floor = models.CharField(max_length=20, blank=True, verbose_name='Этаж')
    square = models.CharField(max_length=20, blank=True, verbose_name='Площадь квартиры')
    address_object = models.CharField(max_length=150, blank=True, verbose_name='Адрес дома')
    number_object = models.CharField(max_length=20, blank=True, verbose_name='Номер дома')
    section_object = models.CharField(max_length=20, blank=True, verbose_name='Секция')
    price = models.CharField(max_length=20, blank=True, verbose_name='Стоимость квартиры')
    price_m = models.CharField(max_length=20, blank=True, verbose_name='Стоимость за 1 кв.м.')
    client_passport_details = models.CharField(max_length=200, blank=True, verbose_name='Паспортные данные клиента')
    place_of_residence = models.CharField(max_length=200, blank=True, verbose_name='Адрес прописки')
    form_of_payment = models.CharField(max_length=150, blank=True, verbose_name='Форма расчёта')
    consult_date = models.CharField(max_length=20, blank=True, verbose_name='Дата консультации')
    consult_time = models.CharField(max_length=20, blank=True, verbose_name='Время консультации')
    manager_select = models.CharField(max_length=150, blank=True, verbose_name='Выбор менеджера')

    add_value_1 = models.CharField(max_length=150, blank=True, verbose_name='Доп. значение 1')
    add_value_2 = models.CharField(max_length=150, blank=True, verbose_name='Доп. значение 2')
    add_value_3 = models.CharField(max_length=150, blank=True, verbose_name='Доп. значение 3')
    add_value_4 = models.CharField(max_length=150, blank=True, verbose_name='Доп. значение 4')
    add_value_5 = models.CharField(max_length=150, blank=True, verbose_name='Доп. значение 5')

    email_message = models.TextField(blank=True, verbose_name='Email текст сообщения')
    attach = models.CharField(max_length=150, blank=True, null=True, verbose_name='Прикреплённый файл')

    def __str__(self):
        return str(self.date_time_send)

    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'
        ordering = ['date_time_send']
