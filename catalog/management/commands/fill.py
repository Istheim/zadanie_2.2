from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        products_list = [
            {'name': 'Коптер', 'description': 'Квадракоптер для безграничных полётов', 'category_id': '1',
             'price': "60200"},
            {'name': 'DELL', 'description': 'Хороший АМЕРИКАНСКИЙ компьюктер', 'category_id': '2', 'price': "92000"},
            {'name': 'Стиральная машина Endesit', 'description': 'Ну а зачем стирать руками? Стирай в машине',
             'category_id': '1', 'price': "60200"},
            {'name': 'Кофемашина', 'description': 'На ней никуда не уехать, но кофе выпить можно', 'category_id': '1',
             'price': "43050"},

        ]

        products_to_create = []
        for product_item in products_list:
            products_to_create.append(Product(**product_item))

        Product.objects.bulk_create(products_to_create)