from django.shortcuts import render

# Create your views here.

from .models import Category, Profuct as Product
from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from django.contrib import messages
from django.contrib.messages import get_messages

def ProductList(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    messages.add_message(request, messages.INFO, 'You were return on the main paige')
    storage = get_messages(request)
    return render(request, 'shop/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products,
        'storage': storage
    })

def ProductDetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})
