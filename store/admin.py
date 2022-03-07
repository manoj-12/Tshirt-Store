
from django.contrib import admin

from store .models .product import  Cart, Order, OrderItem, Payment,Tshirt , NeckType , Occasion , Color ,Idealfor,Brand,Sleeve,Sizevariant,Slider
# Register your models here.

class Sizevariantconfig(admin.StackedInline):
    model = Sizevariant

class Tshirtconfig(admin.ModelAdmin):
    prepopulated_fields = {'slug':('tshirt_name',)}
    inlines = [Sizevariantconfig]
    list_per_page = 12
    list_display = ('tshirt_name','occasion','Ideal_for','neck_type','sleeve','brand','color')

class CartAdmin(admin.ModelAdmin):

    model = Cart
    # fields = ('user',)
    list_display = ['user','quantity']
    fieldsets = (
        ('CART INFORMATION',{
            'fields':('user','sizeVariant','quantity',)
        }),
    )



class orderAdmin(admin.ModelAdmin):
    list_display = ['user','payment_method','shiping_address' ,'phone' ,'total' , 'date']



admin.site.register(Slider)
admin.site.register(Tshirt , Tshirtconfig)
admin.site.register(NeckType)
admin.site.register(Occasion)
admin.site.register(Color)
admin.site.register(Idealfor)
admin.site.register(Brand)
admin.site.register(Sleeve)
admin.site.register(Cart , CartAdmin)
admin.site.register(Order,orderAdmin)
admin.site.register(Payment)
admin.site.register(OrderItem)


