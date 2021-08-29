from django.db import models


class User(models.Model):
    name = models.TextField(verbose_name='Имя')
    address = models.TextField(verbose_name='адрес')
    latitude = models.FloatField(verbose_name='Широта', blank=True, null=True)
    longitude = models.FloatField(verbose_name='Долгота', blank=True, null=True)
    gender = models.BooleanField(verbose_name='Пол')
    age = models.PositiveIntegerField(verbose_name='Возраст')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.name} {self.age}'

    def save(self, *args, **kwargs):
        """
        Function for auto-deocode user's address by means geopy
        """
        from geopy.geocoders import Nominatim
        loc = self.address
        geolocator = Nominatim(user_agent="my_request")
        location = geolocator.geocode(loc)
        self.latitude = location.latitude
        self.longitude = location.longitude
        super(User, self).save(*args, **kwargs)


class Post(models.Model):
    image = models.ImageField(verbose_name="Фото", blank=True, upload_to='blog_images')
    title = models.TextField('Заголовок')
    text = models.TextField('Текст')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title


class Hashtag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField('Текст')

    class Meta:
        verbose_name = 'Хэштег'
        verbose_name_plural = 'Хэштеги'

    def __str__(self):
        return self.text


class Like(models.Model):
    date = models.DateTimeField(verbose_name='Дата', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'

    def __str__(self):
        return f'{self.user} {self.post}'


class Transaction(models.Model):
    date = models.DateTimeField(verbose_name='Дата', auto_now_add=True)
    place = models.TextField(verbose_name='Место')
    sum = models.FloatField(verbose_name='Сумма')

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'

    def __str__(self):
        return f'{self.place} {self.sum}'


class Realty(models.Model):
    sum = models.PositiveIntegerField(verbose_name='Стоимость')
    square = models.PositiveIntegerField(verbose_name='Площадь')
    place = models.TextField(verbose_name='Адрес')
    link = models.TextField(verbose_name='Ссылка')
    latitude = models.FloatField(verbose_name='Широта', blank=True, null=True)
    longitude = models.FloatField(verbose_name='Долгота', blank=True, null=True)

    class Meta:
        verbose_name = 'Недвижимость'
        verbose_name_plural = 'Недвижимость'

    def __str__(self):
        return f'{self.sum} {self.place} {self.link}'

    def save(self, *args, **kwargs):
        """
        Function for auto-deocode realty's address by means geopy
        """
        from geopy.geocoders import Nominatim
        loc = self.place
        geolocator = Nominatim(user_agent="my_request")
        location = geolocator.geocode(loc)
        # self.address_lng = f'{location.latitude} {location.longitude}'
        self.latitude = location.latitude
        self.longitude = location.longitude
        super(Realty, self).save(*args, **kwargs)