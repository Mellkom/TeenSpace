# Generated by Django 5.1.2 on 2024-10-29 10:16

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure_app', '0006_delete_home'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название места')),
                ('descriprion', models.TextField(verbose_name='Об этом месте')),
                ('address', models.CharField(max_length=150, verbose_name='Адрес места')),
                ('salary', models.CharField(max_length=100, verbose_name='Стоимость')),
                ('phone', models.CharField(max_length=17, verbose_name='Номер телефона')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата и время публикации')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adventure_app.category', verbose_name='Выберите категорию')),
            ],
            options={
                'verbose_name': 'Концерт',
                'verbose_name_plural': 'Концерты',
            },
        ),
        migrations.CreateModel(
            name='Kino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название места')),
                ('descriprion', models.TextField(verbose_name='Об этом месте')),
                ('address', models.CharField(max_length=150, verbose_name='Адрес места')),
                ('salary', models.CharField(max_length=100, verbose_name='Стоимость')),
                ('phone', models.CharField(max_length=17, verbose_name='Номер телефона')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата и время публикации')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adventure_app.category', verbose_name='Выберите категорию')),
            ],
            options={
                'verbose_name': 'Кино',
                'verbose_name_plural': 'Кино',
            },
        ),
        migrations.CreateModel(
            name='Musems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название места')),
                ('descriprion', models.TextField(verbose_name='Об этом месте')),
                ('address', models.CharField(max_length=150, verbose_name='Адрес места')),
                ('salary', models.CharField(max_length=100, verbose_name='Стоимость')),
                ('phone', models.CharField(max_length=17, verbose_name='Номер телефона')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата и время публикации')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adventure_app.category', verbose_name='Выберите категорию')),
            ],
            options={
                'verbose_name': 'Музей',
                'verbose_name_plural': 'Музеи',
            },
        ),
        migrations.CreateModel(
            name='Parks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название места')),
                ('descriprion', models.TextField(verbose_name='Об этом месте')),
                ('address', models.CharField(max_length=150, verbose_name='Адрес места')),
                ('salary', models.CharField(max_length=100, verbose_name='Стоимость')),
                ('phone', models.CharField(max_length=17, verbose_name='Номер телефона')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата и время публикации')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adventure_app.category', verbose_name='Выберите категорию')),
            ],
            options={
                'verbose_name': 'Парк',
                'verbose_name_plural': 'Парки',
            },
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название места')),
                ('descriprion', models.TextField(verbose_name='Об этом месте')),
                ('address', models.CharField(max_length=150, verbose_name='Адрес места')),
                ('salary', models.CharField(max_length=100, verbose_name='Стоимость')),
                ('phone', models.CharField(max_length=17, verbose_name='Номер телефона')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата и время публикации')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adventure_app.category', verbose_name='Выберите категорию')),
            ],
            options={
                'verbose_name': 'Спорт',
                'verbose_name_plural': 'Спорт',
            },
        ),
        migrations.DeleteModel(
            name='Places',
        ),
    ]