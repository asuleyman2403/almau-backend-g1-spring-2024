from django.urls import path
from .views import products_page_view, product_details_page_view, delete_product_page_view, edit_product_page_view, \
    index_page_view, category_page_view

urlpatterns = [
    # products/
    path('', index_page_view, name='index_page'),
    path('categories/<int:pk>', category_page_view, name='category_details_page'),
    path('products/', products_page_view, name='products_page'),
    path('products/<int:pk>', product_details_page_view, name='product_details_page'),
    path('products/<int:pk>/edit', edit_product_page_view, name='edit_product_page'),
    path('products/<int:pk>/delete', delete_product_page_view, name='delete_product_page')
]
