import os
import uuid
from django.db import models


def product_preview_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"preview/{uuid.uuid4()}.{ext}"
    return os.path.join('products', filename)


def product_detail_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"original/{uuid.uuid4()}.{ext}"
    return os.path.join('products', filename)


class Category(models.Model):
    name = models.CharField(verbose_name="Название", max_length=100)
    parent = models.ForeignKey(
        'self',
        verbose_name="Родитель",
        help_text="Родительская категория",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    class Meta:
        db_table = 'categories'
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' → '.join(full_path[::-1])

    def as_list(self):
        result = [self]
        k = self.parent
        while k is not None:
            result.append(k)
            k = k.parent
        return result[::-1]

class Brand(models.Model):
    name = models.CharField(verbose_name="Название", max_length=255)
    slug = models.SlugField(help_text="Уникал. индентификатор бренда", unique=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'brands'
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"


class Product(models.Model):
    name = models.CharField(verbose_name="Название", max_length=255)
    description = models.TextField(verbose_name="Описание", blank=True)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, verbose_name="Бренд", on_delete=models.CASCADE)
    nutrition_facts = models.JSONField(verbose_name="Энергетическая ценность", blank=True, null=True)
    slug = models.SlugField(help_text="Уникал. индентификатор товара", unique=True, blank=True)
    weight = models.IntegerField(verbose_name="Вес", null=True)

    img_preview = models.ImageField(verbose_name="Превью фото", upload_to=product_preview_upload_to, default='products/preview/product_no_picture.png')
    img_original = models.ImageField(verbose_name="Оригинальное фото", upload_to=product_detail_upload_to, default='products/original/product_no_picture.png')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'
        unique_together = ('brand', 'slug')
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
