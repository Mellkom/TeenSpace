# Generated by Django 5.1.2 on 2024-10-27 14:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='places',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата и время публикации'),
        ),
    ]