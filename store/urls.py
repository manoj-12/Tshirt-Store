from django .urls import path
from store.views.addcart import AddToCart
from store.views.cartdetail import CartDetail
from store.views.checkout import Checkout,ValidatedPayment
from store.views.orderView import orderView
from store .views .product import home
from store.views.product_detail import ProductDetail

urlpatterns = [
    path('', home, name="homepage"),
    path('productdetail/<str:slug>', ProductDetail , name="productdetail"),
    path('addtocard/<str:slug>/<str:size>' , AddToCart , name="addToCart"),
    path('cartdetail' , CartDetail , name="CartDetail"),
    path('checkout' , Checkout , name="checkout"),
    path('validate_payment' , ValidatedPayment , name="validatedpayment"),
    path('order' , orderView , name="orderView"),
]