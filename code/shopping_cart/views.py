from django.shortcuts import render, get_object_or_404, redirect, reverse
from products.models import Product
from accounts.models import Profile
from shopping_cart.models import OrderItem, Order
from shopping_cart.extras import  generate_order_id
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.defaulttags import register
# Create your views here.
def get_user_pending_order(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    if order.exists():
        return order[0]
    return 0

@login_required()
def add_to_cart(request, **kwargs):
    messages.info(request, "dodano przedmiot do koszyka")
    print("kwargs", kwargs)
    print("request",  request, request.user)
    user_profile = get_object_or_404(Profile, user=request.user)
    if not user_profile:
        if not request.session.get(product.name):
            request.session[product.name] = 1
        else: 
            request.session[product.name] += 1
        print("w sesji ilość przedmiotów {} to {}".format(product.name, request.session[product.name]))
        print("w sesji ilość przedmiotów {} to {}".format('coca cola', request.session['coca cola']))
        print("user_profile", user_profile)
        return redirect(reverse('product-list'))

    product = Product.objects.filter(id=kwargs.get('item_id', "")).first()
    print("request.user.profile.ebooks", request.user.profile.ebooks.all())
    if product in request.user.profile.ebooks.all():
        request.user.profile.ebooks[product.name][0].quantity += 1
        messages.info(request, "Added one more item")
        return redirect(reverse('product-list'))
    
    order_item, status = OrderItem.objects.get_or_create(product=product)

    user_order, status = Order.objects.get_or_create(owner=user_profile)
    user_order.items.add(order_item)
    if status:
        user_order.ref_code = generate_order_id()
        user_order.save()
    user_profile.ebooks.add(product)
    messages.info(request, "item added to cart")
    
    return redirect(reverse('product-list'))

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
        'order_id' : order_id
    }
    return render(request, 'shopping_cart/payment.html', context)

'''
@register.TEMPLATES
def get_item_number(dictionary, key):
    print("wypluje", dictionary.get(key)[0].quantity)
    return dictionary.get(key)[0].quantity
'''