from django.core.cache import cache

from config.settings import CACHE_ENABLED
from catalog.models import Product


def get_products_from_cache(category):
    """Получает список продуктов из кэша по указанной категории. Если кэш пуст, получает из базы данных"""
    if not CACHE_ENABLED:
       return Product.objects.filter(category=category)

    key = f'products_category_{category.pk}'
    products = cache.get(key)
    if products is not None:
        return products

    products = Product.objects.filter(category=category)
    cache.set(key, products)
    return products
