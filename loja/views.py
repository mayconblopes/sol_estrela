import quantity as quantity
from django.shortcuts import render

from loja.models import Product


def index(request):
    products = Product.objects.all().exclude(quantity=0)
    return render(request, 'index.html', {'products': products})


def product_details(request):
    return render(request, 'product_details.html')
