from django.contrib import admin
from django.forms import SelectMultiple, Select, TextInput
from django import forms
from django.db import models

from .models import *


class DistrictAdmin(admin.ModelAdmin):
    """Переопределяем поля Района"""
    class Meta:
        model = District

    list_display = ('name', 'subname')


class HouseOfObjectInline(admin.TabularInline):
    """Подключает отображение Домов на странице Жилого Комплекса"""
    model = HouseOfObject
    formfield_overrides = {models.ManyToManyField: {'widget': SelectMultiple(attrs={'style': 'width:150px',
                                                                                    'class': 'js-example-basic-multiple'})},
                           models.ForeignKey: {'widget': Select(attrs={'style': 'width:150px',
                                                                       'class': 'js-example-basic-single'})},
                           models.CharField: {'widget': TextInput(attrs={'style': 'width:150px'})},
                           }


class HouseOfObjectAdmin(admin.ModelAdmin):
    """Переопределяем поля Дома Объекта"""
    list_display = ('address', 'jk_object', 'deadline', 'floors', 'house_material')
    ordering = ['jk_object']
    # filter_horizontal = ('finishing_flat', 'payment_method', 'bank',)  # встроенный вид SelectMultiple
    formfield_overrides = {
        models.ManyToManyField: {'widget': SelectMultiple(attrs={'size': '5', 'style': 'color:blue;width:250px',
                                                                 'class': 'js-example-basic-multiple'})}, }

    class Media:
        css = {
            'all': ('css/select2.min.css',)
        }
        js = ('js/jquery-3.3.1.min.js',
              'js/select2.min.js',
              'js/main.js',
              )


class JkObjectAdmin(admin.ModelAdmin):
    """Переопределяем поля Жилого Комплекса"""
    class Meta:
        model = JkObject

    class Media:
        css = {'all': ('css/select2.min.css',)}
        js = ('js/jquery-3.3.1.min.js',
              'js/select2.min.js',
              'js/main.js',)

    list_display = ('id', 'name', 'developer', 'district', 'class_building', 'is_active')
    list_display_links = ('name',)
    # ordering = ['id']
    list_editable = ['is_active']
    # fieldsets = (
    #     (None, {'fields': ('name', 'developer', ('district', 'class_building'),)}),
    #     ('Фото объекта', {
    #         # 'classes': ('collapse',),
    #         'fields': ('image',), }),)
    list_filter = ('is_active', 'district', 'class_building',)
    inlines = [HouseOfObjectInline]  # Подключает отображение Домов на странице админке ЖК
    # search_fields = ['=name']
    formfield_overrides = {models.ForeignKey: {'widget': Select(attrs={'style': 'width:20em',
                                                                       'class': 'js-example-basic-single'})}, }


admin.site.register(District, DistrictAdmin)
admin.site.register(DeadlineBuilding)
admin.site.register(Developer)
admin.site.register(HouseMaterial)
admin.site.register(PaymentМethod)
admin.site.register(Bank)
admin.site.register(ClassBuilding)
admin.site.register(FinishingFlat)
admin.site.register(JkObject, JkObjectAdmin)
admin.site.register(HouseOfObject, HouseOfObjectAdmin)
