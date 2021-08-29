# Generated by Django 3.2.6 on 2021-08-29 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyst', '0010_auto_20210828_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='Realty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.PositiveIntegerField(verbose_name='Стоимость')),
                ('square', models.PositiveIntegerField(verbose_name='Площадь')),
                ('place', models.TextField(verbose_name='Адрес')),
                ('link', models.TextField(verbose_name='Ссылка')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='Широта')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='Долгота')),
            ],
            options={
                'verbose_name': 'Недвижимость',
                'verbose_name_plural': 'Недвижимость',
            },
        ),
        migrations.AlterModelOptions(
            name='hashtag',
            options={'verbose_name': 'Хэштег', 'verbose_name_plural': 'Хэштеги'},
        ),
    ]
