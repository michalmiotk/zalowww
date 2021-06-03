from django.conf.urls import url
from django.urls import path
from .views import product_list, product_detail
from django.utils.translation import gettext_lazy as _
app_name = "products"

product_urlpatterns = [
    path(_('products/'), product_list, name='product-list'),
    path(_('product_detail/<int:id>'), product_detail, name='product-detail'),
]