from math import prod
from django.shortcuts import render, get_object_or_404, redirect, reverse
from products.models import Product
from accounts.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.defaulttags import register

from django.views.decorators.http import require_POST
from shopping_cart.cart import Cart
from shopping_cart.forms import CartAddProductForm

@require_POST
def cart_add(request, item_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=item_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
            quantity=cd['quantity'],
            update_quantity=cd['update'])
    return redirect(reverse('product-list'))

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={"quantity": item['quantity'],
                     'update': True}
        )
    return render(request, 'shopping_cart/detail.html', {'cart': cart})

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect(cart_detail)
    
