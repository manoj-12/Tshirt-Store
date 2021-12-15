from django.urls import path
from store .views .product import home


urlpatterns = [
    path('' , home , name="homepage")
]