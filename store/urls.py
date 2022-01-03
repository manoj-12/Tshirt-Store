from django .urls import path
from store .views .product import home
from store .views .product_detail import ProductDetail

urlpatterns = [
    path('', home, name="homepage"),
    path('productdetail/<str:slug>', ProductDetail , name="productdetail"),
]