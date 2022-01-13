from django.shortcuts import redirect
from store.models.product import Cart, Sizevariant, Tshirt

def AddToCart(request , slug , size):
    user = None
    if request.user.is_authenticated:
        user = request.user
    cart = request.session.get('cart')
    

    if cart is None:
        cart = []
    tshirt = Tshirt.objects.get(slug=slug)
    size_temp= Sizevariant.objects.get(size=size , tshirt=tshirt)

    flag = True
    for cartobj in cart:
        t_id=cartobj.get('tshirt')
        size_short=cartobj.get('size')
        if t_id == tshirt.id and size == size_short:
        # if t_id == tshirt.id and size == cartobj['size']:
            flag = False
            cartobj['quantity']=  cartobj['quantity']+1

    if flag:
        cart_obj = {
            'tshirt':tshirt.id,
            'size':size,
            'quantity':1,
        }
        cart.append(cart_obj)

    if user is not None:
        existing = Cart.objects.filter(user=user , sizeVariant=size_temp)    
        if len(existing)>0:
            obj = existing[0]
            obj.quantity = obj.quantity+1 
            obj.save()   
        else:
            c = Cart()
            c.user = user
            c.sizeVariant = size_temp
            c.quantity = 1
            c.save()




    
        
    request.session['cart'] = cart
    Retun_Url = request.GET.get('full_path')
    # print('Cart Session =:',request.session.get('cart'))
    return redirect(Retun_Url)