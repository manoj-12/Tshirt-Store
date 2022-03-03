
from django .shortcuts import render , HttpResponse
from django.core.paginator import Paginator
from math  import floor
from store .models .product import Slider, Tshirt , Occasion , Sleeve , NeckType , Idealfor,Brand,Color
from urllib.parse import urlencode



def home(request):
    slider = Slider.objects.all()
    print("Slider :",slider)
    data = request.GET
    tshirt = Tshirt.objects.all()

    occations = data.get('occation')
    sleeves = data.get('sleeve')
    neck_types = data.get('neck_type')
    ideal_fors = data.get('ideal_for')
    brands = data.get('brand')
    colors = data.get('color')



    if occations !='' and occations is not None:
        tshirt = tshirt.filter(occasion__slug = occations)

    if sleeves !='' and sleeves is not None:
        tshirt = tshirt.filter(sleeve__slug = sleeves)

    if neck_types !='' and neck_types is not None:
        tshirt = tshirt.filter(neck_type__slug = neck_types)
    
    if ideal_fors !='' and ideal_fors is not None:
        tshirt = tshirt.filter(Ideal_for__slug = ideal_fors)

    if brands !='' and brands is not None:
        tshirt = tshirt.filter(brand__slug = brands)

    if colors !='' and colors is not None:
        tshirt = tshirt.filter(color__slug = colors)
        
    occation = Occasion.objects.all()
    sleve = Sleeve.objects.all()
    neck_type = NeckType.objects.all()
    ideal_for = Idealfor.objects.all()
    color = Color.objects.all()
    brand = Brand.objects.all()

      
    paginator = Paginator(tshirt, 12) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    data = request.GET.copy()
    data['page']= ''
    pageurl = urlencode(data)
    context = {
        'sliders':slider,
        'occations':occation,
        'sleeves':sleve,
        'neck_types':neck_type,
        'ideal_fors':ideal_for,
        'colors':color,
        'brands':brand,
        'page_obj':page_obj,
        'pageurl':pageurl
    }
    return render(request , 'index.html' , context=context)


