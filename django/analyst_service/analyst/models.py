from django.db import models


class Transaction(models.Model):
    date = models.DateTimeField(verbose_name='Дата транзакции')
    place = models.TextField(verbose_name='Место')
    sum = models.FloatField(verbose_name='Сумма')

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'


class User(models.Model):
    address = models.TextField(verbose_name='адрес')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'