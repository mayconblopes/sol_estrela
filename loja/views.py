from django.shortcuts import render, get_object_or_404

from loja.models import Product


def index(request):
    products = Product.objects.all().exclude(in_stock=False)
    return render(request, 'index.html', {'products': products})


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)

    # MSFList to str
    size = ', '.join([item for item in product.size])
    size_label = 'Tamanhos' if len(product.size) > 1 else 'Tamanho'

    # product price can be intallment if price is greater than 50
    if product.sell_price > 50.00:
        # installment price on 5x times / preço parcelado em 5x vezes
        installments_on_credit = float(product.credit_price) / 5
        installments_on_credit = f'{installments_on_credit:.2f}'.replace('.', ',')  # -> 8,48 instead of 8.4833333333
    else:
        installments_on_credit = False

    return render(request, 'product_details.html', {'product': product,
                                                    'size': size,
                                                    'size_label': size_label,
                                                    'installments_on_credit': installments_on_credit})


def girls_products(request):
    products = Product.objects.all().exclude(in_stock=False).exclude(genre='MENINO')
    return render(request, 'index.html', {'products': products,
                                          'filter_class': 'MENINA',
                                          'filter_icon': 'girl_icon.png', })


def boys_products(request):
    products = Product.objects.all().exclude(in_stock=False).exclude(genre='MENINA')
    return render(request, 'index.html', {'products': products,
                                          'filter_class': 'MENINO',
                                          'filter_icon': 'boy_icon.png', })


def payment(request):
    return render(request, 'payment.html')


def contact(request):
    return render(request, 'contact.html')