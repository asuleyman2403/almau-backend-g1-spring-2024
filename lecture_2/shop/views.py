from django.shortcuts import render
from .models import Product


def get_ingex_page(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def get_product_details(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'shop/product-details.html', {'product': product})


