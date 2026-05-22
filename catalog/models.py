from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Наименование',
        help_text='Укажите название категории'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание',
        help_text='Введите описание категории'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Наименование',
        help_text='Укажите наименование товара')
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание',
        help_text='Введите описание товара'
    )
    image = models.ImageField(
        upload_to='catalog/images/',
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение товара",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name='Категория',
        help_text='Укажите категорию товара',
        null=True,
        blank=True,
        related_name="catalog",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена за покупку',
        help_text='Укажите цену за покупку товара',
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name = 'Дата создания',
        null = True,
        blank = True
    )
    updated_at = models.DateField(
        auto_now=True,
        verbose_name='Дата последнего изменения',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
