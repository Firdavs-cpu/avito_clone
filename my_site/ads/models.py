from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    slug = models.SlugField(max_length=120, unique=True, verbose_name='URL-префикс')

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


    def __str__(self):
        return self.name
    

class AD(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads', verbose_name='Продавц')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='ads',verbose_name='Категории')
    title = models.CharField(max_length=100, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена (Руб).')
    image = models.ImageField(upload_to='ads_images/', blank=True, null=True, verbose_name="Фотография")
    is_active = models.BooleanField(default=True, verbose_name="Активно (не продано)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ['-created_at']  # Свежие всегда вверху

    def __str__(self):
        return self.title


