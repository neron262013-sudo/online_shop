from datetime import date

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок", help_text="Введите заголовок поста")
    content = models.TextField(verbose_name="Контент", help_text="Напишите ваш пост")
    preview = models.ImageField(
        upload_to="blog/images/", blank=True, null=True, verbose_name="Изображение", help_text="Изображение для поста"
    )
    posted_by = models.DateField(
        verbose_name="Дата публикации",
        help_text="Укажите дату публикации",
        default=date.today,
    )
    is_published = models.BooleanField(
        default=False, verbose_name="Опубликован", help_text="Отметьте, если пост опубликован"
    )
    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )
