from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import UserProfile


# admin.site.register(UserProfile)


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Доп. информация'


class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('username',
                    'email',
                    # 'first_name',
                    # 'last_name',
                    'is_staff',
                    # 'is_superuser',
                    'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'password', 'email')}),
        # (('Personal info'), {
        #     'fields': ('first_name', 'last_name', 'email')
        # }),
        (('Permissions'), {
            'classes': ('collapse',),
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        (('Important dates'), {
            'classes': ('collapse',),
            'fields': ('last_login', 'date_joined')
        }),
    )
    list_editable = ['is_active']
    inlines = (UserProfileInline,)

    class Meta:
        model = User

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        # Если у пользователя есть доступ в админку запрещаем для него отображение суперпользователя
        return qs.filter(is_superuser=False)

    def get_readonly_fields(self, request, obj=None):
        # Запрещённые поля для редактирования для пользователя с доступом в админку
        return () if request.user.is_superuser else ('is_staff', 'is_superuser', 'groups', 'user_permissions')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


