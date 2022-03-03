
from django.contrib import admin
from django.utils.html import format_html

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



    # readonly_fields = ('user',)



class orderAdmin(admin.ModelAdmin):
    list_display = ['user','shiping_address','payment_method','total','phone','date']

    readonly_fields = ('user',
                       'shiping_address',
                       'payment_method',
                       'phone',
                       'total',
                       'payment',
                       'payment_request_id',
                       'payment_id',
                       'payment_status'
                       )
    fieldsets = (
        ('ORDER INFORMATION', {'fields': ('order_status','shiping_address','phone','total','user')}),
        ('PAYMENT INFORMATION', {'fields': ('payment_request_id','payment_id','payment','payment_status')})
    )

    def payment_request_id(self,obj):
        return obj.payment_set.all()[0].payment_request_id

    def payment_id(self,obj):
        return obj.payment_set.all()[0].payment_id


    def payment_status(self,obj):
        return obj.payment_set.all()[0].payment_status

    def payment(self,obj):
        p_id = obj.payment_set.all()[0].id
        return format_html( f"<a href='/admin/store/payment/{p_id}/change/' target='_blank'>Click For Payment Informantion</a>")


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


