from store .urls import path
from django .shortcuts import HttpResponse , render

def home(request):
    print(request.user)
    return render(request , 'index.html')

