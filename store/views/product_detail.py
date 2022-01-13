from django .shortcuts import render
from store.models.product import Tshirt
from math import floor

def ProductDetail(request , slug):
    # print('ID = :',id)
    tshirt = Tshirt.objects.get(slug=slug)
    size = request.GET.get('size')
    if size == None:
        size = tshirt.sizevariant_set.all().order_by('price').first()
    else:
        size = tshirt.sizevariant_set.get(size=size)
    # print('detail Page Size',size)
    price = size.price
    discount = tshirt.discount
    sale_price = floor(price - (price*discount/100))
    # print('Size Price :',size.price)
    context={
        'tshirt':tshirt,
        'saleprice':sale_price,
        'price':price,
        'active_size':size
    }
    return render(request , 'product_detail.html',context=context)


