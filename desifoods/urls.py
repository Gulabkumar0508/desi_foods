from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('contact_us',views.contact_view,name='contact'),
    path('food', views.food, name='food'),
    path('about_us', views.about, name='about'),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart-detail/', views.cart_detail, name='cart_detail'),
    path('checkout',views.checkout,name='checkout'),
    path('food/<str:id>', views.product_detail, name='product_detail'),
]
