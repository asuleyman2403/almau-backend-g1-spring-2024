from django.urls import path
from .views import product_details_view, products_page_view, delete_product_page_view, index_page_view


urlpatterns = [
    # products/
    path('', index_page_view, name='index_page'),
    path('products/', products_page_view, name='products'),
    path('products/<int:pk>', product_details_view, name='product_details'),
    path('products/<int:pk>/delete', delete_product_page_view, name='delete_product_page')
]

