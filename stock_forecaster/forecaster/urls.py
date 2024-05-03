from django.urls import path
from . import views

urlpatterns = [
    path('constructModel/', views.constructModel, name='constructModel')
]