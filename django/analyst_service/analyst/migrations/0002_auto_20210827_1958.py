# Generated by Django 3.2.6 on 2021-08-27 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyst', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='address_lng',
            field=models.TextField(default=1, verbose_name='адрес'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(default=1, verbose_name='Возраст'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.TextField(default=1, verbose_name='Пол'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата'),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('post', models.ManyToManyField(to='analyst.Post')),
                ('user', models.ManyToManyField(to='analyst.User')),
            ],
            options={
                'verbose_name': 'Лайк',
                'verbose_name_plural': 'Лайки',
            },
        ),
    ]
