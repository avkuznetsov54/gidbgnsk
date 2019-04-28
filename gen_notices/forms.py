from django import forms
from .models import Notice
from .models import Office


class NoticeForm(forms.ModelForm):
    developer = forms.CharField()
    jk_object = forms.CharField()
    emails_developer = forms.CharField()
    office = forms.ModelChoiceField(queryset=Office.objects.all(),
                                    required=False)
    fio_client = forms.CharField()
    phone_client = forms.CharField()
    fio_agent = forms.CharField()
    phone_agent = forms.CharField()
    email_agent = forms.CharField()

    sum_of_rooms = forms.CharField(required=False)
    apartment_number = forms.CharField(required=False)
    floor = forms.CharField(required=False)
    square = forms.CharField(required=False)
    address_object = forms.CharField(required=False)
    number_object = forms.CharField(required=False)
    section_object = forms.CharField(required=False)
    price = forms.CharField(required=False)
    price_m = forms.CharField(required=False)
    client_passport_details = forms.CharField(required=False)
    place_of_residence = forms.CharField(required=False)
    form_of_payment = forms.CharField(required=False)
    consult_date = forms.CharField(required=False)
    consult_time = forms.CharField(required=False)
    manager_select = forms.CharField(required=False)

    attach = forms.Field(widget=forms.FileInput, required=False)

    type_for_lawyer = forms.CharField(required=False)
    type_for_notice = forms.CharField(required=False)

    email_message = forms.CharField()

    class Meta(object):
        model = Notice
        fields = ('developer',
                  'jk_object',
                  'emails_developer',
                  'office',
                  'fio_client',
                  'phone_client',
                  'fio_agent',
                  'phone_agent',
                  'email_agent',
                  'sum_of_rooms',
                  'apartment_number',
                  'floor',
                  'square',
                  'address_object',
                  'number_object',
                  'section_object',
                  'price',
                  'price_m',
                  'client_passport_details',
                  'place_of_residence',
                  'form_of_payment',
                  'consult_date',
                  'consult_time',
                  'manager_select',
                  'attach',
                  'type_for_lawyer',
                  'type_for_notice',
                  'email_message')
