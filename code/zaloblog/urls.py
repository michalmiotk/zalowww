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
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, include
from home.views import home_view, read_article
from about.views import about_view
from pricing.views import pricing_view
from shopping_cart.views import cart_add, cart_detail, cart_remove
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.i18n import i18n_patterns
from products.urls import product_urlpatterns
from login.views import login_gui, login_machine, my_logout
from my_register.views import register_view
from orders.urls import order_urlpatterns
from coupons.urls import coupon_urlpatterns
from django.utils.translation import gettext_lazy as _
urlpatterns = i18n_patterns(
    url(r'^rosetta/', include('rosetta.urls')),
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
    path('$', home_view, name="home"),
    path('<str:slug>', read_article),
    path(_('pricing/'), pricing_view),
    path(_('about/'), about_view),
    url(_(r'^cart_detail/'), cart_detail, name='cart_detail'),
    path(_(r'add-to-cart/(?P<item_id>\d+)/'), cart_add, name="cart_add"),
    url(_(r'^cart_remove/(?P<product_id>\d+)/$'),cart_remove, name="cart_remove"),
    path(_(r'login/'),login_gui),
    path(_(r'login_machine/'), login_machine),
    path(_('register/'), register_view, name="register_view"),
    path(_("logout/"), my_logout, name="logout"),
    url(_(r'^paypal/'), include('paypal.standard.ipn.urls')),
    url(_(r'^payment/'), include('payment.urls',namespace='payment')),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns.extend(product_urlpatterns)
urlpatterns.extend(order_urlpatterns)
urlpatterns.extend(coupon_urlpatterns)

#to ponizej musi byc ladowane jako ostatnie bo inaczej jest problem ze nie widzi tego co jest ponizej
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


