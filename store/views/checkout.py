from math import floor
from django .shortcuts import render , redirect , HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.form.authform import CheckoutForm
from store.models.product import Cart, Order, OrderItem, Payment
from instamojo_wrapper import Instamojo
from Tstore .settings import API_KEY , AUTH_TOKEN
API = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/')


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
            # print('Quantity',quantity)
            single_prod=price-(price*discount/100)
            final_price = single_prod*quantity
            # print('Final Price:',final_price)
            # print('Single Product:',single_prod)
            total = floor(total+final_price)
            # print("Total",total)
        context = {
            'form':form,
            'carts':cart,
            'total':total
        }
        return render(request , 'checkout.html' , context=context)
    # Post Request
    else:
        form = form = CheckoutForm(request.POST)
        if form .is_valid():
            shiping_add = form.cleaned_data.get('shiping_address')
            phone = form.cleaned_data.get('phone')
            payment_method = form.cleaned_data.get('payment_method')
            print('shiping_add :',shiping_add,'phone :',phone,'payment_method :',payment_method)
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
            order.order_status = "PANDING"
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
            response = API.payment_request_create(
                amount=order.total,
                purpose='sale Tshirt',
                buyer_name=user.first_name,
                send_email=True,
                email= user.email,
                redirect_url="http://localhost:8000/validate_payment"
            )

            print('Payment Request =:',response['payment_request'])
            payment_request_id = response['payment_request']['id']
            url = response['payment_request']['longurl']
            payment = Payment()
            payment.order=order
            payment.payment_request_id = payment_request_id
            payment.save()
            return redirect(url)
        else:
            return redirect('/checkout')

def ValidatedPayment(request):
    user = None
    if request.user.is_authenticated:
        user = request.user
    payment_id = request.GET.get('payment_id')
    payment_request_id = request.GET.get('payment_request_id')
    print('payment_id :',payment_id)
    print('payment_request_id :',payment_request_id)
    # Create a new Payment Request
    response = API.payment_request_payment_status(payment_request_id,payment_id)
    status = response['payment_request']['payment']['status']
    print('Status -:',status)

    if status != 'Failed':
        payment = Payment.objects.get(payment_request_id=payment_request_id)
        payment.payment_id = payment_id
        payment.payment_status = status
        payment.save()

        order = payment.order
        order.order_status = 'PLACED'
        order.save()

        cart = []
        request.session['cart'] = cart
        cart = Cart.objects.filter(user=user).delete()
        return redirect('/order')
    return render(request , 'paymntfail.html')
