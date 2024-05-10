from django.contrib import admin
from django.urls import path, include, re_path

from .import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('login_check/', views.login_check, name='login_check'),
    path('send_message/', views.send_message, name='send_message'),
    path('lehenga/', views.lehenga, name='lehenga'),
    path('saree/', views.saree, name='saree'),
    path('navari/', views.navari, name='navari'),
    path('suit/', views.suit, name='suit'),
    path('redimade/', views.redimade, name='redimade'),
    path('charge/', views.charge, name='charge'),
    # path('cart/', views.cart, name='cart'),



    # re_path('edit_check/(?P<id>[0-9]+)/$', views.edit_check, name='edit_check'), 
    re_path('edit_check/(?P<id>[0-9]+)/$', views.edit_check, name='edit_check' ),





]
