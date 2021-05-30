"""zaloblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from home.views import home_view, read_article
from about.views import about_view
from pricing.views import pricing_view
from shopping_cart.views import cart_add, cart_detail, cart_remove
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from products.urls import product_urlpatterns
from login.views import login_gui, login_machine, my_logout
from my_register.views import register_view
from orders.urls import order_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
    path('$', home_view, name="home"),
    path('<str:slug>', read_article),
    path('pricing/', pricing_view),
    path('about/', about_view),
    url(r'^cart_detail/', cart_detail, name='cart_detail'),
    path(r'add-to-cart/(?P<item_id>\d+)/', cart_add, name="cart_add"),
    url(r'^cart_remove/(?P<product_id>\d+)/$',cart_remove, name="cart_remove"),
    path(r'login/',login_gui),
    path(r'login_machine/', login_machine),
    path('register/', register_view, name="register_view"),
    path("logout/", my_logout, name="logout"),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(r'^payment/', include('payment.urls',namespace='payment')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns.extend(product_urlpatterns)
urlpatterns.extend(order_urlpatterns)

