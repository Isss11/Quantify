from django.urls import path
from . import views

urlpatterns = [
    path('arimaForecast/', views.arimaForecast, name='arimaForecast'),
    path('stockTickers', views.stockTickers, name='stockTickers')
]