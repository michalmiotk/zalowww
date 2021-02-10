from django.shortcuts import render, get_object_or_404, redirect, reverse
from products.models import Product
from accounts.models import Profile
from shopping_cart.models import OrderItem, Order
from shopping_cart.extras import  generate_order_id
from django.contrib.auth.decorators import login_required

# Create your views here.
def get_user_pending_order(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    if order.exists():
        return order[0]
    return 0

@login_required()
def add_to_cart(request, **kwargs):
    user_profile = get_object_or_404(Profile, user=request.user)
    product = Product.objects.filter(id=kwargs.get('item_id', "")).first()
    if product in request.user.profile.ebooks.all():
        messages.info(request, "You already own this ebook")
        return redirect(reverse('products:product-list'))
    
    order_item, status = OrderItem.objects.get_or_create(product=product)

    user_order, status = Order.objects.get_or_create(owner=user_profile)
    user.order.items.add(order_item)
    if status:
        user_order.ref_code = generate_order_id()
        user_order.save()
    
    message.info(request, "item added to cart")
    return redirect(reverse('products:product-list'))

@login_required
def delete_from_cart(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Item has been deleted")
    return redirect(reverse('shopping_cart:order_summary'))

@login_required()
def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'shopping_cart/order_summary.html', context)