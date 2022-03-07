from math import floor
from django .shortcuts import render , redirect , HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.form.authform import CheckoutForm
from store.models.product import Cart, Order, OrderItem, Payment
from Tstore .settings import API_KEY , AUTH_TOKEN
from instamojo_wrapper import Instamojo
API = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/');



@login_required(login_url='/accounts/login')
def Checkout(request):
    # Get Request
    if request.method=='GET':
        form = CheckoutForm()
        user =  request.user
        cart = Cart.objects.filter(user=user)
        total = 0
        for c in cart:
            price = c.sizeVariant.price
            discount = c.sizeVariant.tshirt.discount
            quantity = c.quantity
            single_prod=price-(price*discount/100)
            final_price = single_prod*quantity
            total = floor(total+final_price)
        context = {
            'form':form,
            'carts':cart,
            'total':total
        }
        return render(request , 'checkout.html' , context=context)
    # Post Request
    else:
        form = CheckoutForm(request.POST)
        if form .is_valid():
            shiping_add = form.cleaned_data.get('shiping_address')
            phone = form.cleaned_data.get('phone')
            payment_method = form.cleaned_data.get('payment_method')
            # print('shiping_add :',shiping_add,'phone :',phone,'payment_method :',payment_method)
            user =  request.user
            cart = Cart.objects.filter(user=user)
            total = 0
            for c in cart:
                tshirt = c.sizeVariant.tshirt
                print('Tshirt :',tshirt)
                size = c.sizeVariant
                print('Size :',size)
                quantity = c.quantity
                print('QUANTITY :',quantity)
                price = c.sizeVariant.price
                discount = c.sizeVariant.tshirt.discount
                quantity = c.quantity
                # print('Quantity',quantity)
                single_prod=price-(price*discount/100)
                final_price = single_prod*quantity
                # print('Final Price:',final_price)
                # print('Single Product:',single_prod)
                total = floor(total+final_price)
            print("Total",total)
            order = Order()
            order.payment_method = payment_method
            order.phone = phone
            order.shiping_address = shiping_add
            order.user = user
            order.total = total
            order.save()


            
            # Saving Order Item
            for c in cart:
                tshirt = c.sizeVariant.tshirt
                size = c.sizeVariant
                quantity = c.quantity
                price = c.sizeVariant.price
                discount = c.sizeVariant.tshirt.discount
                single_prod=price-(price*discount/100)
                order_item = OrderItem()
                order_item.order = order
                order_item.tshirt = tshirt
                order_item.size = size
                order_item.quantity = quantity
                order_item.price = single_prod 
                order_item.save()
            cart = []
            request.session['cart'] = cart
            Cart.objects.filter(user=user).delete()
            return redirect('/order')

        else:
            return redirect('/checkout')



