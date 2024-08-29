from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('login/', views.login_view, name='login'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('seller_home/', views.seller_home, name='seller_home'),
    path('admin_home/logout/', views.logout_page),
    path('seller_home/logout/', views.logout_page),
]
