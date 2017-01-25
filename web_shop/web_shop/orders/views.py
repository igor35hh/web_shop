from django.shortcuts import render

# Create your views here.

from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.shortcuts import get_object_or_404
from .models import Order
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def AdminOrderDetail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/orders/order/detail.html', {'order': order})

def OrderCreate(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if cart.cupon:
                order.cupon = cart.cupon
                order.discount = cart.cupon.discount
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'], quantity=item['quantity'])
            cart.clear()
            return render(request, 'orders/order/created.html', {'cart':cart, 'order':order})
        
    form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart':cart, 'form':form})
