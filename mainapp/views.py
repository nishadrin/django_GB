from django.shortcuts import render
from .models import Product, ProductCategory

# Create your views here.
links_main_menu = [
{
    'href': 'index', 'name': 'Главная'
},
{
    'href': 'catalog', 'name': 'Каталог'
},
{
    'href': 'contacts', 'name': 'Контакты'
}
]
def index(request):
    context = {
        "title_page": 'Интернет магазин',
        'links_main_menu': links_main_menu
    }
    return render(request, 'mainapp/index.html', context)

def contacts(request):
    contact_locations = [
    {
        'city': 'санкт-Петербург',
        'phone': '+7 (812) 1234567',
        'email': 'spb@bestseller.ru',
        'address': 'ленина, д.1',
    },
    {
        'city': 'москва',
        'phone': '+7 (479) 1234567',
        'email': 'moscow@bestseller.ru',
        'address': 'пушкина, д.1',
    },
    ]
    context = {
        "title_page": 'Контакты',
        'contact_locations': contact_locations,
        'links_main_menu': links_main_menu
    }
    return render(request, 'mainapp/contacts.html', context)

def catalog(request):
    products = Product.objects.all()
    product_cat = ProductCategory.objects.all()
    context = {
        "title_page": 'Каталог',
        "products": products,
        'links_main_menu': links_main_menu,
        'product_cat': product_cat,
    }
    return render(request, 'mainapp/catalog.html', context)
