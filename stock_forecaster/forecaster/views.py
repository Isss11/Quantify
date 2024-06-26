from django.shortcuts import render
from django.http import HttpResponse
from . import ARIMAForecaster, LSTMForecaster, StockDetail
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
# Constructs a ARIMA model to forecast stock returns, using ML
@api_view(['POST'])
def arimaForecast(request):
    requestValues = JSONParser().parse(request)
    forecaster = ARIMAForecaster.ARIMAForecaster(requestValues["ticker"], requestValues["sampleStartDate"])
    
    # Obtains the actual approximated percentage returns from the training data forecasted returns
    modelDetails = forecaster.createModel()
    returns = forecaster.getCombinedReturns(requestValues["forecastLength"])
    
    response = dict(returns)
    response['modelDetails'] = modelDetails
    
    # Allowing non-dictionary values to serialized by setting safe equal to false
    return JsonResponse(response)

@api_view(['POST'])
def lstmForecast(request):
    requestValues = JSONParser().parse(request)
    
    # Creating model with given look-back amount
    forecaster = LSTMForecaster.LSTMForecaster(requestValues["ticker"], requestValues["sampleStartDate"])
    forecaster.createModel(requestValues["lookBack"], requestValues["epochs"], requestValues["batchSize"])
    
    # Getting prices and model accuracy details to include in response
    prices = forecaster.getCombinedPrices(requestValues['forecastLength'])
    modelAccuracy, modelDetails = forecaster.getModelAccuracy()
    modelParameters = {"modelType": "LSTM", "stock": requestValues["ticker"], "forecastLength": requestValues["forecastLength"], "lookBack": requestValues["lookBack"], "epochs": requestValues["epochs"], "batchSize": requestValues["batchSize"]}
    
    response = dict({"parameters": modelParameters, "details": modelDetails, "prices": prices, "modelAccuracy": modelAccuracy})
    
    return JsonResponse(response)
    

# Returns general stock information used in the UI
@api_view(['POST'])
def stockDetail(request, stockTicker):
    stockInfo = StockDetail.StockDetail(str(stockTicker))
    
    return JsonResponse(stockInfo.getGeneralInfo())