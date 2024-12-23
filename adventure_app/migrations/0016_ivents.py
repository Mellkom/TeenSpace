# Generated by Django 5.1.2 on 2024-10-29 17:09

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure_app', '0015_concert_image_kino_image_musems_image_parks_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ivents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название места')),
                ('image', models.ImageField(blank=True, upload_to='image')),
                ('descriprion', models.TextField(verbose_name='Об этом месте')),
                ('address', models.CharField(max_length=150, verbose_name='Адрес места')),
                ('salary', models.CharField(max_length=100, verbose_name='Стоимость')),
                ('phone', models.CharField(max_length=17, verbose_name='Номер телефона')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата и время публикации')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adventure_app.category', verbose_name='Выберите категорию')),
            ],
            options={
                'verbose_name': 'Ивент',
                'verbose_name_plural': 'Ивенты',
            },
        ),
    ]
