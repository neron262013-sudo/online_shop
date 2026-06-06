from django.contrib import admin
from django.core.exceptions import ValidationError
from PIL import Image

from catalog.models import Category, Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    list_filter = ("category",)
    search_fields = (
        "name",
        "description",
    )
    fields = ("name", "description", "image", "category", "price")

    def save_model(self, request, obj, form, change):
        if obj.image:
            try:
                img = Image.open(obj.image)
                img.verify()
            except Exception:
                raise ValidationError("Можно загружать только изображения")

        super().save_model(request, obj, form, change)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
