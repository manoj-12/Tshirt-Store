from django.contrib import admin
from store .models .product import Tshirt , NeckType , Occasion , Color ,Idealfor,Brand,Sleeve,Sizevariant
# Register your models here.

class Sizevariantconfig(admin.StackedInline):
    model = Sizevariant

class  Tshirtconfig(admin.ModelAdmin):
    inlines = [Sizevariantconfig]

admin.site.register(Tshirt , Tshirtconfig)
admin.site.register(NeckType)
admin.site.register(Occasion)
admin.site.register(Color)
admin.site.register(Idealfor)
admin.site.register(Brand)
admin.site.register(Sleeve)

