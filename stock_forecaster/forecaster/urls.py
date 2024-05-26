from django.urls import path
from . import views

urlpatterns = [
    path('arimaForecast/', views.arimaForecast, name='arimaForecast'),
    path('lstmForecast/', views.lstmForecast, name='lstmForecast'),
    path('stockDetail/<stockTicker>/', views.stockDetail, name='stockDetail'),
]