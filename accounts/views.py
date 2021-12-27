
from django.shortcuts import render, redirect
from accounts.form.authform import CustometCreationForm, CustomerLoginForm
from django.contrib.auth import authenticate, login as loginUser , logout as LogOut



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
               loginUser(request,user) #save login user in session by loginUser
               return  redirect('/')
        else:
            return render(request, 'login.html', {'form': form})




def logout(request):
    LogOut(request)
    return redirect('/')
