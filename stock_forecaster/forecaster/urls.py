from django.urls import path
from . import views

urlpatterns = [
    path('arimaForecast/', views.arimaForecast, name='arimaForecast'),
    path('stockDetail/<stockTicker>/', views.stockDetail, name='stockDetail'),
]