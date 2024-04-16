from django.urls import path, include
from . import views
from django.conf import settings
from weather import views as weather_views

urlpatterns = [
  path('', views.IndexView, name = 'index'),
  path('register/', views.RegisterView, name = 'register'),
  path('login/', views.LoginView, name = 'login'),
  path('logout/', views.LogOutView, name ='logout'),
  path('weather/', weather_views.weather, name = "weather"),
]
