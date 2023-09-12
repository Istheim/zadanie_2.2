from django.core.management import BaseCommand, call_command

from catalog.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        Product.objects.all().delete()
        call_command('loaddata', '../hw_19.2/data.json')