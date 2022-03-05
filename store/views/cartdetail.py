from math import floor
from django.shortcuts import render

from store.models.product import Sizevariant, Tshirt



def CartDetail(request):
    total = 0
    cart = request.session.get('cart')
    if cart is None:
        cart = []
    for c in cart:
        t_id = c.get('tshirt')
        t_size = c.get('size')
        tshirt = Tshirt.objects.get(id=t_id)
        c['tshirt']=tshirt
        c['size'] = Sizevariant.objects.get(tshirt=t_id , size=t_size)
        discount = tshirt.discount
        price = c['size'].price
        # quantity = c['quantity']
        quantity = c.get('quantity')
        single_prod_price = price -(price*discount/100)
        sale_price = single_prod_price*quantity
        total = floor(total+sale_price)
   
    return render(request , 'cart_detail.html',{'carts':cart , 'total':total})