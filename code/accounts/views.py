from django.shortcuts import render
from shopping_cart.models import Order
from .models import Profile
# Create your views here.

def my_profile(request):
    my_user_profile = Profile.objects.filter(user=request.user).first()
    my_orders = Order.objects.filter(is_ordered=True, owner=my_user_profile)
    context = {
        'my_orders':my_orders
    }

    return render(request, "profile.html", context)