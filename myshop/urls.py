from django.contrib import admin
from django.urls import path
from .views import*
from .ajax import *
from users.views import*
app_name='myshop'
urlpatterns = [
    path('',home,name='home'),
    path('Logout/',logouts,name="logouts"),
    path('Error/',erorr,name='error'),
    path('Blog/',blog,name='blog'),
    path('Checkout/',checkout,name='checkout'),
    path('Blog-details/',blog_details,name='blog-details'),
    # path('Category/',category,name='category'),
    path('Contact/',contact,name='contact'),
    path('Faq/',faq,name='faq'),
    path('My-wishlist/',my_wishlist,name='my-wishlist'),
    path('Product-comparison/',product_comparison,name='product-comparison'),
    path('Shopping-cart/',cart_detail.as_view(),name='shopping-cart'),
    path('Sign-in/',UserView.as_view(),name='sign-in'),
    path('terms-conditions/',terms_conditions,name='terms-conditions'),
    path('track-orders/',track_orders,name='track-orders'),
    # path('Category/',Defcategory,name='category'),
    path('Wrapper/',Wrapper,name='Wrapper'),
    path('<sub_slug>/',Subcategory_product.as_view(),name='subcategory_product'),
    path('add_to_cart',cart_add,name='add_to_cart'),
    path('shop_cart',shop_cart,name='shop_cart'),
    path('detail/<int:pk>',ProductDetail.as_view(),name='detail'),
    path('delete',cart_delete,name='cart_delete'),
    path('Change_cart',Change_cart,name='Change_cart'),
    path('Search_products',Search_products,name='search_products'),
    path('District_Provice',District_Provice,name='District_Provice'),
    
]