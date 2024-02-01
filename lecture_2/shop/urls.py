from django.contrib import admin
from django.urls import path

from .views import get_ingex_page, get_product_details

urlpatterns = [
    path('', get_ingex_page),
    path('<int:pk>', get_product_details)
]
