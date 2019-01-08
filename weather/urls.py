from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('weather/<city_name>', views.weather, name='weather')
]

