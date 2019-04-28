from django.contrib import admin
from .models import ContractOrg


class ContractOrgAdmin(admin.ModelAdmin):
    """Переопределяем поля Района"""
    class Meta:
        model = ContractOrg

    search_fields = ['number_1c']
    list_display = ('number_1c', 'rooms', 'street', 'num_house', 'district', 'floor', 'num_of_floors', 'house_material',
                    'type_flat', 'all_square', 'living_square', 'kitchen_square', 'price', 'num_flat', 'developer')


admin.site.register(ContractOrg, ContractOrgAdmin)
