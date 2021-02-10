from django.shortcuts import render
from products.models import Product
from shopping_cart.models import Order
# Create your views here.

def product_list(request):
    object_list = Product.objects.all()
    print(object_list)
    filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=True)
    current_order_products = []

    if filtered_orders.exists():
        user_order = filtered_orders[0]
        user_order_items = user_order.items.all()
        current_order_products = [product.product for product in user_order_items]

    context = {
        'object_list': object_list,
        'current_order_products': current_order_products
    }

    return render(request, "products/products_list.html", context)