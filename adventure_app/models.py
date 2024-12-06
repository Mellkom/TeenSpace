from django.db import models
from pytils.translit import slugify
from datetime import datetime
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    image = models.ImageField(blank=True, upload_to='image')
    name = models.CharField("Название категории", max_length=255)
    slug = models.SlugField(unique=True, editable=False, blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
class Vakanсy(models.Model):
    name = models.CharField("Название компании", max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Выберите категорию")
    author = models.CharField("Работодатель", max_length=255)
    cost = models.CharField("Зарплата", max_length=150)
    phone = models.CharField("Номер телефона", max_length=17)
    course = models.URLField("Ссылка на курсы", max_length=500)

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return self.name