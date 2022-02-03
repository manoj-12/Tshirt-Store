
from django.shortcuts import render, redirect
from accounts.form.authform import CustometCreationForm, CustomerLoginForm
from django.contrib.auth import authenticate, login as loginUser , logout as LogOut
from store .models .product import Cart, Sizevariant

# Create your views here.


def signup(request):
    if request.method == 'GET':
        form = CustometCreationForm()
        return render(request, 'signup.html' , {'form':form})
   
    form = CustometCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.email = user.username
        user.save()
        print(user)
        return redirect('loginform')
    else:
        return render(request, 'signup.html' ,{'form':form})
   
def login(request):
    next_page = request.GET.get('next')
    # print('Next Page',next_page)
    if request.method == 'GET':
        form = CustomerLoginForm()
        return render(request , 'login.html' ,{'form':form})
    else:
        form = CustomerLoginForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username , password=password)
            if user:
                loginUser(request,user)
                session_cart = request.session.get('cart')
                if session_cart is None:
                    session_cart = []
                else:
                    for c in session_cart:
                        size = c.get('size')
                        tshirt = c.get('tshirt')
                        quantity = c.get('quantity')
                        cart_obj = Cart()
                        cart_obj.sizeVariant = Sizevariant.objects.get(size=size , tshirt=tshirt)
                        cart_obj.quantity = quantity
                        cart_obj.user = user
                        cart_obj.save()
                cart = Cart.objects.filter(user=user)
                session_cart = []
                for c in cart:
                   obj = {
                    'size':c.sizeVariant.size,
                    'tshirt':c.sizeVariant.tshirt.id,
                    'quantity':c.quantity
                    }
                   session_cart.append(obj)
                request.session['cart']=session_cart
                if next_page is None:
                    return redirect('/')
                else:
                    return redirect (next_page)
        else:
            return render(request, 'login.html', {'form': form})

def logout(request):
    LogOut(request)
    return redirect('/')
