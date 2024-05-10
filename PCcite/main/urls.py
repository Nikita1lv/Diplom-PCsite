from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name = "home"),
    path('about', views.about, name = "about"),
    path('map', views.map, name = "map"),
    path('profile',profile_view, name="profile"),
    path('register', RegisterView.as_view(),name="register"),
    path('product/<int:product_id>/', product, name='product'),
    path('cart/', cart, name='cart'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('order/', order, name='order'),
    path('order_add/<int:product_id>/', order_add, name='order_add'),
]