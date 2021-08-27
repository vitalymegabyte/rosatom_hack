from django.db import models


class User(models.Model):
    name = models.TextField(verbose_name='Имя')
    address = models.TextField(verbose_name='адрес')
    address_lng = models.TextField(verbose_name='адрес(Кординаты)')
    gender = models.TextField(verbose_name='Пол')
    age = models.PositiveIntegerField(verbose_name='Возраст')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Post(models.Model):
    title = models.TextField('Заголовок')
    text = models.TextField('Текст')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Like(models.Model):
    date = models.DateTimeField(verbose_name='Дата', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'


class Transaction(models.Model):
    date = models.DateTimeField(verbose_name='Дата', auto_now_add=True)
    place = models.TextField(verbose_name='Место')
    sum = models.FloatField(verbose_name='Сумма')

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'

