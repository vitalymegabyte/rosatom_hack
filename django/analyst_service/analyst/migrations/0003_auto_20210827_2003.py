# Generated by Django 3.2.6 on 2021-08-27 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyst', '0002_auto_20210827_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.TextField(default=234, verbose_name='Имя'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='address_lng',
            field=models.TextField(verbose_name='адрес(Кординаты)'),
        ),
    ]
