from django.conf.urls import url

from .views import product_list

app_name = "products"

product_urlpatterns = [
    url(r'^products/$', product_list, name='product-list')
]