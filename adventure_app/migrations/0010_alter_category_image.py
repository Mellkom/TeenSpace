# Generated by Django 5.1.2 on 2024-10-29 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure_app', '0009_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
