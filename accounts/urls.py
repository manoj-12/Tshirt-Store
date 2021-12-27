from django.urls import path
# from accounts  .views import signup
from accounts import views


urlpatterns = [
    path('signup' ,views.signup, name="signup"),
    path('login', views.login , name="loginform"),
    path('logout', views.logout , name='logout')
]