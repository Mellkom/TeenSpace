# Generated by Django 5.1.2 on 2024-10-27 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure_app', '0002_places_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='places',
            old_name='title',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='places',
            name='phone',
            field=models.CharField(max_length=17, verbose_name='Номер телефона'),
        ),
    ]