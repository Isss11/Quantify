from django.shortcuts import render
from django.http import HttpResponse
from . import ARIMAForecaster
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

# Constructs a ARIMA model to forecast stock returns, using ML
@api_view(['POST'])
def arimaForecast(request):
    requestValues = JSONParser().parse(request)
    forecaster = ARIMAForecaster.ARIMAForecaster(requestValues["ticker"])
    
    # Obtains the actual approximated percentage returns from the training data forecasted returns
    forecaster.createModel()
    forecastedReturns = forecaster.getForecasts(requestValues["forecastLength"])
    
    return HttpResponse(str(forecastedReturns))