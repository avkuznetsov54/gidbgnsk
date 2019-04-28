from django.contrib import admin

from .models import AdditionalValue
from .models import Office
from .models import Notice
from .models import NoticeTemplate


class AdditionalValueAdmin(admin.ModelAdmin):
    class Meta:
        model = AdditionalValue

    list_display = ('name', 'description', 'value')


class OfficeAdmin(admin.ModelAdmin):
    class Meta:
        model = Office

    list_display = ('office', 'name_rop', 'email')


class NoticeAdmin(admin.ModelAdmin):
    class Meta:
        model = Notice

    list_display = ('date_time_send', 'developer', 'jk_object', 'fio_client', 'fio_agent', 'office')
    ordering = ['-date_time_send']


class NoticeTemplateAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('nick_name',
                           # 'jk_object',
                           'emails_developer',
                           'file_template',
                           'file_null_notice',
                           'type_for_lawyer_is_active',
                           'type_for_notice_choice',
                           'office_is_active',
                           ('fio_client', 'fio_client_is_active'),
                           ('phone_client', 'phone_client_is_active'),
                           ('fio_agent', 'fio_agent_is_active'),
                           ('phone_agent', 'phone_agent_is_active'),
                           ('email_agent', 'email_agent_is_active'),
                           ('sum_of_rooms', 'sum_of_rooms_is_active'),
                           ('apartment_number', 'apartment_number_is_active'),
                           ('floor', 'floor_is_active'),
                           ('square', 'square_is_active'),
                           ('address_object', 'address_object_is_active'),
                           ('number_object', 'number_object_is_active'),
                           ('section_object', 'section_object_is_active'),
                           ('price', 'price_is_active'),
                           ('price_m', 'price_m_is_active'),
                           ('client_passport_details', 'client_passport_details_is_active'),
                           ('place_of_residence', 'place_of_residence_is_active'),
                           ('form_of_payment', 'form_of_payment_is_active'),
                           ('consult_date', 'consult_date_is_active'),
                           ('consult_time', 'consult_time_is_active'),
                           ('manager_select', 'manager_select_is_active'),
                           )}),
        ('Дополнительные значения', {'classes': ('collapse',),
                                     'fields': (
                                         ('add_value_1', 'add_value_1_is_active'),
                                         ('add_value_2', 'add_value_2_is_active'),
                                         ('add_value_3', 'add_value_3_is_active'),
                                         ('add_value_4', 'add_value_4_is_active'),
                                         ('add_value_5', 'add_value_5_is_active'),
                                                ), }),)

    class Meta:
        model = NoticeTemplate

    # fieldsets = ((None, {'fields': ('nick_name',
    #                        'jk_object',
    #                        'office_is_active',
    #                        'fio_client_is_active',
    #                        'phone_client_is_active',
    #                        'fio_agent_is_active',
    #                        'phone_agent_is_active',
    #                        'email_agent_is_active',
    #                        'sum_of_rooms_is_active',
    #                        'apartment_number_is_active',
    #                        'floor_is_active',
    #                        'square_is_active',
    #                        'address_object_is_active',
    #                        'number_object_is_active',
    #                        'section_object_is_active',
    #                        'price_is_active',
    #                        'price_m_is_active',
    #                        'client_passport_details_is_active',
    #                        'place_of_residence_is_active',
    #                        'form_of_payment_is_active',
    #                        'consult_date_is_active',
    #                        'consult_time_is_active',
    #                        'manager_select_is_active',
    #                        'file_template',
    #                        )}),)

    # exclude = ['office',
    #            # 'fio_client',
    #            'phone_client',
    #            'fio_agent',
    #            'phone_agent',
    #            'email_agent',
    #            'sum_of_rooms',
    #            'apartment_number',
    #            'floor',
    #            'square',
    #            'address_object',
    #            'number_object',
    #            'section_object',
    #            'price',
    #            'price_m',
    #            'client_passport_details',
    #            'place_of_residence',
    #            'form_of_payment',
    #            'consult_date',
    #            'consult_time',
    #            'manager_select',
    #            'type_for_lawyer',
    #            'type_for_notice'
    #            ]


admin.site.register(AdditionalValue, AdditionalValueAdmin)
admin.site.register(Office, OfficeAdmin)
admin.site.register(NoticeTemplate, NoticeTemplateAdmin)
admin.site.register(Notice, NoticeAdmin)
