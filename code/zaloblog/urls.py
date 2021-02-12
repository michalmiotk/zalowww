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
from django.urls import path
from home.views import home_view, read_article
from about.views import about_view
from pricing.views import pricing_view
from shopping_cart.views import add_to_cart, order_details, delete_from_cart,delete_from_cart,checkout, payment
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from products.urls import product_urlpatterns
from login.views import login_gui, login_machine
from my_register.views import register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
    path('$', home_view, name="home"),
    path('<str:slug>', read_article),
    path('pricing/', pricing_view),
    path('about/', about_view),
    path(r'^add-to-cart/(?P<item_id>[-\w]+)/$', add_to_cart, name="add_to_cart"),
    path(r'^order-summary/$', order_details, name="order_summary"),
    #path(r'^success/$', success, name='purchase_success'),
    path(r'^item/delete/(?P<item_id>[-\w]+)/$', delete_from_cart, name='delete_item'),
    path(r'login/',login_gui),
    path(r'login_machine/', login_machine),
    path(r'^checkout/$', checkout, name='checkout'),
    path(r'^payment/(?P<order_id>[-\w]+/)$', payment, name="process_payment"),
    path('register/', register_view, name="register_view"),
    #path(r'^update-transaction/(?P<order_id>[-\w]+)/$', update_transaction_records, name='update_records'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns.extend(product_urlpatterns)
