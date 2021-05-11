from django.shortcuts import render, get_object_or_404, redirect, reverse
from products.models import Product
from accounts.models import Profile
from shopping_cart.models import OrderItem, Order
from shopping_cart.extras import  generate_order_id
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
    
# Create your views here.
def get_user_pending_order(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    if order.exists():
        return order[0]
    return 0



@login_required
def delete_from_cart(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Item has been deleted")
    return redirect(reverse('order_summary'))

@login_required()
def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'shopping_cart/order_summary.html', context)

@login_required
def checkout(request, **kwargs):
    context = {
        'order' : get_user_pending_order(request)
    }
    return render(request, 'shopping_cart/checkout.html', context)

@login_required
def payment(request, order_id):
    context = {
        'order_id' : order_id,
    }
    return render(request, 'shopping_cart/payment.html', context)

'''
@register.TEMPLATES
def get_item_number(dictionary, key):
    print("wypluje", dictionary.get(key)[0].quantity)
    return dictionary.get(key)[0].quantity
'''