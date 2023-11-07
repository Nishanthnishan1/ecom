from django.urls import path
from . import views
from django.contrib.auth.views import LoginView




urlpatterns=[
    path('',views.home,name='hm'),
    path('<slug:c_slug>/',views.home,name='prod_cat'),
    path('<slug:c_slug>/<slug:product_slug>',views.prodDetails,name='details'),
    path('item',views.item,name='item'),
    path('search',views.searching,name='search'),
    path('login',views.login,name='login'),
    path('register',views.registration,name='register'),
    path('index',views.index,name='index'),
    
]