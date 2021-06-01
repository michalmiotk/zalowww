from django.conf.urls import url
from . import views

coupon_urlpatterns = [
    url(r'^apply/$', views.coupon_apply, name='coupon_apply'),
]