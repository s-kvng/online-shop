from django.shortcuts import render

# Create your views here.

def product_list(request):

    return render(request, "shop/product/list.html")


def product_detail(request):

    return render(request, "shop/product/detail.html")   