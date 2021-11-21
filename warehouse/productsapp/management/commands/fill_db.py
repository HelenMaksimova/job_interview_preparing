from django.core.management.base import BaseCommand
from productsapp.models import Product, Vendor
import random


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='?', type=int, default=5)

    def handle(self, *args, **options):
        product_count = options.get('count')
        vendor_count = random.randint(1, product_count)

        vendors = [Vendor(
            name=f'Поставщик_{idx:02}',
            description=f'Описание поставщика {idx:02}'
        ) for idx in range(1, vendor_count + 1)]
        Vendor.objects.bulk_create(vendors)

        vendors_list = Vendor.objects.all()

        products = [Product(
            name=f'Продукт_{idx:02}',
            price=random.randint(1, 1000) * 100,
            vendor_name=random.choice(vendors_list)
        ) for idx in range(1, product_count + 1)]
        Product.objects.bulk_create(products)

        print('Завершено')
