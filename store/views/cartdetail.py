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
        # print('Discount cartdetail',discount)

        price = c['size'].price
        # print('Price :-',price)
        quantity = c['quantity']
        # print('Quantity :-',quantity)
        single_prod_price = price -(price*discount/100)
        # print('single_prod_price',single_prod_price)
        sale_price = single_prod_price*quantity
        # print('sale_price -:',sale_price)
        total = floor(total+sale_price)
    # print('Total Sale Price',total)
    # print(cart)
    return render(request , 'cart_detail.html',{'carts':cart , 'total':total})