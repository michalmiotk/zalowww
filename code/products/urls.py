from django.conf.urls import url
from django.urls import path
from .views import product_list, product_detail

app_name = "products"

product_urlpatterns = [
    path('products/', product_list, name='product-list'),
    path('product_detail/<int:id>', product_detail, name='product-detail'),
]