from django.urls import path
from shop.views import checkout, confirmation, detail, index, login_user, register_user

urlpatterns = [
    path('', index, name='home'),
    path('<int:product_id>', detail, name="detail"),
    path('checkout', checkout, name="checkout"),
    path('confirmation', confirmation, name="confirmation"),
    path("login/", login_user, name="login"),
     path("register/", register_user, name="register"),
]
