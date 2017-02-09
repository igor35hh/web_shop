from django.shortcuts import render

# Create your views here.

from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.shortcuts import get_object_or_404
from .models import Order
from django.contrib.admin.views.decorators import staff_member_required

from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
import smtplib

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

def OrderEmail(order_id):
    order = get_object_or_404(Order, id=order_id)
    filename = settings.STATIC_ROOT+'order_{}.pdf'.format(order.id)
    CreatePDF(filename, order_id)
    
    subject = 'Thanks for your order'
    message = 'The identifier your order is: {}'.format(order.id)
    to_list = [order.email]

    mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, to_list)
    mail.attach_file(filename)
    mail.send()
    #send_mail(subject, message, settings.EMAIL_HOST_USER, to_list, fail_silently=True)

@staff_member_required
def AdminOrderPDF(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    filename = settings.STATIC_ROOT+'order_{}.pdf'.format(order.id)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename={}'.format(filename)

    CreatePDF(response, order_id)
    
    return response

def CreatePDF(file_or_response, order_id):
    order = get_object_or_404(Order, id=order_id)

    c = canvas.Canvas(file_or_response, pagesize=letter)

    c.setLineWidth(.3)
    c.setFont('Helvetica', 12)
     
    c.drawString(30,750,'Order: {}'.format(order.id))
    c.drawString(30,730,'Created: {}'.format(order.created))
    is_paid = ''
    if order.paid:
        is_paid = 'Is paid'
    else:
       is_paid = 'Is not paid' 
    c.drawString(30,710,'Paid: {}'.format(is_paid))
    total_cost = sum(item.get_cost() for item in order.items.all())
    c.drawString(30,690,'Total: {}'.format(total_cost))
    
    c.drawString(420,750,'Customer: {}'.format(order.first_name+" "+order.last_name))
    c.drawString(420,730,'E-mail: {}'.format(order.email))
    c.drawString(420,710,'Address: {}'.format(order.address))

    c.drawString(250,650,'Ordered products')

    c.drawString(30,600,'Product')
    c.drawString(250,600,'Price')
    c.drawString(350,600,'Quantity')
    c.drawString(450,600,'Total cost')
    c.line(570,595,30,595)

    num_row = 600
    for item in order.items.all():
        num_row -= 20
        c.drawString(30,num_row,'{}'.format(item.product.name))
        c.drawString(250,num_row,'{}'.format(item.price))
        c.drawString(350,num_row,'{}'.format(item.quantity))
        c.drawString(450,num_row,'{}'.format(item.price * item.quantity))

    
    c.showPage()
    c.save()
    
    return file_or_response
    
