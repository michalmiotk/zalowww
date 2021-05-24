from django.shortcuts import render, redirect
from django.urls import reverse
from .models import OrderItem

from .forms import OrderCreateForm
from shopping_cart.cart import Cart

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity'])
            request.session['order_id'] = order.id
            cart.clear()
            return redirect(reverse('payment:process'))