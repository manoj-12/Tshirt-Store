from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from store.models.product import Order, OrderItem

@login_required(login_url='/accounts/login')
def orderView(request):
    user = request.user
    order = Order.objects.filter(user=user).order_by('-date').exclude(order_status='PANDING')
    context = {
        'orders':order
    }
    return render(request, 'order.html', context=context)