# from store .urls import path
from django .shortcuts import HttpResponse , render
from math  import floor
from store .models .product import Sizevariant, Tshirt

def home(request):
    tshirt = Tshirt.objects.all()
    context = {
        'tshirts':tshirt,
    }
    return render(request , 'index.html' , context=context)

