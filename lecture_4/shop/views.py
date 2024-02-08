from django.shortcuts import render, redirect
from .models import Product
from .forms import CreateProductForm
from django.contrib import messages


def index_page_view(request):
    return redirect('/products')


def products_page_view(request):
    if request.method == 'GET':
        form = CreateProductForm()
        products = Product.objects.all()
        return render(request, 'shop/index.html', {'products': products, 'form': form})
    if request.method == 'POST':
        print(request.POST)
        # name = request.POST.get('name', '')
        # description = request.POST.get('description', '')
        # amount = request.POST.get('amount', 0)
        # price = request.POST.get('price', 0)

        form = CreateProductForm(request.POST)

        if form.is_valid():
            name = form.data.get('name')
            description = form.data.get('description')
            amount = form.data.get('amount')
            price = form.data.get('price')
            product = Product(name=name, description=description, amount=amount, price=price)
            product.save()
        products = Product.objects.all()
        return render(request, 'shop/index.html', {'products': products, 'form': form})


def product_details_view(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'shop/product_detail.html', {'product': product})


def delete_product_page_view(request, pk):
    try:
        product = Product.objects.get(id=pk)
        product.delete()
        return redirect('/products')
    except Product.DoesNotExist:
        error = 'Product not Found'
        messages.error(request, message=error)
        return redirect('/products')


