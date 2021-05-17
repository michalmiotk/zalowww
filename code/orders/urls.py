from django.conf.urls import url
from . import views

order_urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create')
]