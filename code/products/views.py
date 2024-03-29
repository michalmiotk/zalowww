from django.shortcuts import get_object_or_404, render
from products.models import Product
from shopping_cart.forms import CartAddProductForm
# Create your views here.

def product_list(request):
    object_list = Product.objects.all()
    cart_product_form = CartAddProductForm()
    context = {
        'object_list': object_list,
        'cart_product_form': cart_product_form
    }

    return render(request, "products/product_list.html", context)

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "products/product_detail.html", {'product': product})