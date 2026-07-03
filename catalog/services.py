from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


def get_products_from_cache(category):
    """Получает список продуктов из кэша по указанной категории. Если кэш пуст, получает из базы данных"""
    if not CACHE_ENABLED:
        return Product.objects.filter(category=category)

    key = f"category_{category.pk}"
    products = cache.get(key)

    if products is None:
        products = Product.objects.filter(category=category)
        cache.set(key, products, 60 * 5)

    return products
