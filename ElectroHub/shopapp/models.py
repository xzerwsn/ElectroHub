from django.contrib.auth.models import AbstractUser
from django.db import models

class ShopUser(AbstractUser):
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    address = models.TextField(verbose_name='Адрес', blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Баланс')

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'