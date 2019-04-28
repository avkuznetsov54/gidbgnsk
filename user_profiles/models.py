from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE,
                                    verbose_name='Имя пользователя',
                                    unique=True)
    full_name = models.CharField(max_length=255, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)

    def __unicode__(self):
        return self.full_name

    def __str__(self):
        return str(self.username)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
