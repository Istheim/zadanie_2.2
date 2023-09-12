from django.conf import settings
from django.core.cache import cache

from catalog.models import Category, Product


def get_cached_subjects_from_product(product_pk):
    if settings.CACHE_ENABLED:
        key = f'product_list_{product_pk}'
        product_list = cache.get(key)
        if product_list is None:
            product_list = Product.objects.filter(product__pk=product_pk)
            cache.set(key, product_list)
        else:
            product_list = Product.objects.filter(product__pk=product_pk)
        return product_list


def get_cached_categories():
    if settings.CACHE_ENABLED:
        key = "categories"
        categories_list = cache.get(key)
        if categories_list is None:
            categories_list = Category.objects.all()
            cache.set(key, categories_list)
    else:
        categories_list = Category.objects.all()

    return categories_list