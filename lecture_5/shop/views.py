from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import CreateProductForm, ProductForm
from django.contrib import messages


def index_page_view(request):
    categories = Category.objects.all()
    return render(request, 'shop/index.html', {'categories': categories})


def products_page_view(request):
    categories = Category.objects.all()
    if request.method == 'GET':
        form = ProductForm()
        products = Product.objects.all()
        return render(request, 'shop/products.html', {'products': products, 'form': form, 'categories': categories})
    if request.method == 'POST':
        print(request.POST)
        # name = request.POST.get('name', '')
        # description = request.POST.get('description', '')
        # amount = request.POST.get('amount', 0)
        # price = request.POST.get('price', 0)

        form = ProductForm(request.POST)

        if form.is_valid():
            name = form.data.get('name')
            description = form.data.get('description')
            amount = form.data.get('amount')
            price = form.data.get('price')
            category_id = form.data.get('category')
            product = Product(name=name, description=description, amount=amount, price=price, category_id=category_id)
            product.save()
        products = Product.objects.all()
        return render(request, 'shop/products.html', {'products': products, 'form': form,  'categories': categories})


def product_details_view(request, pk):
    if request.method == 'GET':
        product = Product.objects.get(id=pk)

        return render(request, 'shop/product-detail.html', {'product': product})


def category_products_view(request, pk):
    category = Category.objects.get(id=pk)
    products = Product.objects.filter(category_id=pk)

    if request.method == 'GET':
        form = CreateProductForm()
        return render(request, 'shop/category-products.html',
                      {'category': category, 'products': products, 'form': form})

    if request.method == 'POST':
        form = CreateProductForm(request.POST)
        if form.is_valid():
            name = form.data.get('name')
            description = form.data.get('description')
            amount = form.data.get('amount')
            price = form.data.get('price')
            print(category)
            product = Product(name=name, description=description, amount=amount, price=price, category_id=category.id)
            product.save()
        products = Product.objects.all()
        return render(request, 'shop/category-products.html',
                      {'category': category, 'products': products, 'form': form})


def edit_product_view(request, pk):
    if request.method == 'GET':
        product = Product.objects.get(id=pk)
        form = ProductForm(data={'name': product.name, 'amount': product.amount, 'price': product.price,
                                 'description': product.description})
        return render(request, 'shop/edit-product.html', {'product': product, 'form': form})
    if request.method == 'POST':
        form = ProductForm(request.POST)
        product = Product.objects.get(id=pk)
        if form.is_valid():
            name = form.data.get('name')
            description = form.data.get('description')
            amount = form.data.get('amount')
            price = form.data.get('price')
            product.name = name
            product.description = description
            product.amount = amount
            product.price = price
            product.save()
            return redirect(f'/products/{product.id}')


def delete_product_page_view(request, pk):
    try:
        product = Product.objects.get(id=pk)
        product.delete()
        return redirect('/products')
    except Product.DoesNotExist:
        error = 'Product not Found'
        messages.error(request, message=error)
        return redirect('/products')
