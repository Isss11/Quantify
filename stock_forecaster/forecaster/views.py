from django.shortcuts import render
from django.http import HttpResponse
from . import ARIMAForecaster

# Constructs a ARIMA model to forecast stock returns, using ML
def arimaForecast(request):
    forecaster = ARIMAForecaster.ARIMAForecaster("C")
    
    # Obtains the actual approximated percentage returns from the training data, and the 15 days of forecasted returns
    forecaster.createModel()
    forecastedReturns = forecaster.getForecasts(15)
    
    
    return HttpResponse(str(forecastedReturns))
