from django.shortcuts import render , get_object_or_404 ,redirect
from django.views.decorators.http import require_POST
from shop.models import Product , Category
from .form import CartAddProductForm
from .cart import Cart

# Create your views here.

@require_POST
def cart_add(request, product_id):

    cart = Cart(request)
    product = get_object_or_404(Product , id = product_id)

    form = CartAddProductForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                quantity=cd['quantity'],
                 override_quantity=cd['override'])

    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request,product_id):

    cart = Cart(request)
    product = get_object_or_404(Product , id = product_id)
    cart.remove(product)

    return redirect('cart:cart_detail')



def cart_detail(request):

    print("\n===cart_detail(view)=== -> ")
    cart = Cart(request)

    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
                                            'quantity' : item['quantity'],
                                            'override' : True
                                        })

    categories = Category.objects.all()

    return render(request , 'cart/detail.html' , {'cart': cart, 'categories' : categories})


@require_POST
def cart_clear(request):

    cart = Cart(request)
    cart.clear()

    return redirect('shop:product_list')



    
