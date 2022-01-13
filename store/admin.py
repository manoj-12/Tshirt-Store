from django.contrib import admin
from store .models .product import Cart, Order, OrderItem, Payment, Tshirt , NeckType , Occasion , Color ,Idealfor,Brand,Sleeve,Sizevariant
# Register your models here.

class Sizevariantconfig(admin.StackedInline):
    model = Sizevariant
   

class Tshirtconfig(admin.ModelAdmin):
    prepopulated_fields = {'slug':('tshirt_name',)}
    inlines = [Sizevariantconfig]
    

class CartAdmin(admin.ModelAdmin):
    list_display = ('sizeVariant','quantity','user')


admin.site.register(Tshirt , Tshirtconfig )
admin.site.register(NeckType)
admin.site.register(Occasion)
admin.site.register(Color)
admin.site.register(Idealfor)
admin.site.register(Brand)
admin.site.register(Sleeve)
admin.site.register(Cart , CartAdmin)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(OrderItem)


