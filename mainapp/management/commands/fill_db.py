from django.core.management.base import BaseCommand
from mainapp.models import Product, ProductCategory
from authapp.models import ShopUser

import json, os

JSON_PATH = 'mainapp/json'

def loadFromJSON(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)

class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = loadFromJSON('categories')

        ProductCategory.objects.all().delete()
        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

        products = loadFromJSON('products')

        Product.objects.all().delete()
        for product in products:
            category_name = product["category"]
            # Получаем категорию по имени
            category_ = ProductCategory.objects.get(name=category_name)
            # Заменяем название категории объектом
            product['category'] = category_
            new_product = Product(**product)
            new_product.save()

        # Создаем суперпользователя при помощи менеджера модели
        dele = ShopUser.objects.all().delete()
        create_user = ShopUser.objects.create_superuser('admin', 'admin@admin.local', 'admin', age=21)
