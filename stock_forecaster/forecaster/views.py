from django.shortcuts import render
from django.http import HttpResponse
from . import ARIMAForecaster

# Constructs a ARIMA model to forecast stock returns, using ML
def constructModel(request):
    forecaster = ARIMAForecaster.ARIMAForecaster("C")
    
    # Obtains the actual approximated percentage returns from the training data, and the 15 days of forecasted returns
    stockReturns = forecaster.createModel()
    
    
    return HttpResponse(str(forecaster.stockPrices))
