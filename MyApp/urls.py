from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.index,name="index"),
    path('home',views.home,name="Home page"),
    path('login',views.login,name="login"),
]