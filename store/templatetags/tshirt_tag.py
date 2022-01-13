from django import template
from math import floor

register = template.Library()


@register.simple_tag
def min_price(tshirt):
    min_size = tshirt.sizevariant_set.all().order_by('price').first()
    min_price = min_size.price
    return floor(min_price)

@register.simple_tag
def sale_price(tshirt):
    price = min_price(tshirt)
    discount = tshirt.discount
    return floor(price-(price*discount/100))
    

@register.simple_tag
def rupee():
    return f'₹'    



@register.simple_tag
def ActiveSize(active_size , size):
    if active_size == size:
        return 'dark'
    return 'light'   


@register.simple_tag
def clc_sale_price(price , discount):
    price = price-(price*discount/100)
    return floor(price)

@register.simple_tag
def quantity(a , b):
    return a*b    
 