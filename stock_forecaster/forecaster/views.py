from django.shortcuts import render
from django.http import HttpResponse
from . import ARIMAForecaster, GetTickers
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status

# Constructs a ARIMA model to forecast stock returns, using ML
@api_view(['POST'])
def arimaForecast(request):
    requestValues = JSONParser().parse(request)
    forecaster = ARIMAForecaster.ARIMAForecaster(requestValues["ticker"])
    
    # Obtains the actual approximated percentage returns from the training data forecasted returns
    forecaster.createModel()
    forecastedReturns = forecaster.getForecasts(requestValues["forecastLength"])
    
    # Allowing non-dictionary values to serialized by setting safe equal to false
    return JsonResponse(forecastedReturns.to_json(), status=status.HTTP_200_OK, safe=False)

# Gets all the valid stock tickers to send back to the UI
@api_view(['GET'])
def stockTickers(request):
    return JsonResponse(GetTickers.getTickers(), status=status.HTTP_200_OK, safe=False)