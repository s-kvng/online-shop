from django.shortcuts import render
from .forms import OrderCreateForm
from .models import OrderItem
from cart.cart import Cart
from shop.models import Category

# Create your views here.


def order_cart(request):

    categories = Category.objects.all()
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price = item['price'],
                                        quantity=item['quantity'])
            
            cart.clear()

            return render(request, 'orders/order/created.html', {'order':order})
    
    else:
        form = OrderCreateForm()



    return render(request, 'orders/order/create.html', {'categories':categories, 'form':form, 'cart':cart})

