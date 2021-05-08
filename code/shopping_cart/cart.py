from decimal import Decimal
from django.conf import settings
from products.models import Product

class Cart(object):
    def __init__(self, request):
        self.session = request.session        
        cart = self.session.get(settings.CART_SESSION_ID)
        print(f"settings.CART_SESSION_ID {settings.CART_SESSION_ID} {cart}")
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}  
        self.cart = cart
    
    def add(self, product, quantity=1, update_quantity=False):
        '''
        Dodanie produktu do koszyka lub zmiana jego ilości
        '''
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0, 'price':product.price}

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()
        
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
        
    def __iter__(self):
        '''
        Iteracja przez elementy koszyka na zakupy i pobranie produktów z bazy danych
        '''
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product
        
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
        
    def __len__(self):
        '''
        Obliczenie liczby wszystkich elementów w koszyku na zakupy
        '''
        
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        return sum(Decimal(item['price'])*item['quantity'] for item in self.cart.values())
    
    def clear(self):
        #usunięcie koszyka na zakupy z sesji.
        
        del self.session[settings.CART_SESSION_ID]
        self.session.modified =True