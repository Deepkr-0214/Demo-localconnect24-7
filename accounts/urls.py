from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_customer, name='register_customer'),
    path('register-shop/', views.register_shop, name='register_shop'),
    path('login/', views.login, name='login'),
    path('customer-dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('shop-dashboard/', views.shop_dashboard, name='shop_dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout.html', views.checkout, name='checkout_html'),
    path('help/', views.help, name='help'),
]
