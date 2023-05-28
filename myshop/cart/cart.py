from decimal import Decimal
from django.contrib import settings
from shop.models import Product



class Cart:
    def __init__(self, request):

        """
        Initialize the cart.
        """

        #retrieve and store the current session
        self.session = request.session

        #get the cart with the session key('cart')
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            #save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart


    def add(self, product , quantity=1 , override_quatity=False):

        """
        Add a product to the cart or update its quantity.
        """

        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity' : 0 , 'price' : str(product.price)}

        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()


    def save():
        #mark the session as modified to make sure it get saved 
        self.session.modified = True

    
    def remove(self , product):

        """
        Remove a product from the cart.
        """
        product_id = str(product.id)

        if product_id is in self.cart:
            del self.cart[product_id]
            self.save()


    def __iter__(self):

        """
            Iterate over the items in the cart and get the products
            from the database.
        """

        product_ids = self.cart.keys()  

        #get the product objects and add them to cart
        products = Product.objects.filter(id__in = product_ids)
        cart = self.cart.copy()

        for product in products:

            #add product object to cart
            cart[str(product.id)]['product'] = product
        
        for item in carts.items():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
            


    def __len__(self):
        """
            count all items in the cart
        """

        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price():

        return sum( Decimal(item['price'] * item['quantity'])  for item in self.cart.values())


    def clear():
        
        del self.session[settings.CART_SESSION_ID]
        self.save()