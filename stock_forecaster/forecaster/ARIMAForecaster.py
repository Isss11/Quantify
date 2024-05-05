import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.tsa.stattools as tsa
import statsmodels.tsa.arima.model as arima
import statsmodels.graphics.tsaplots as tsaPlots
import yfinance as yf

# Uses Auto-regressive Integrated Moving Average Model to perform short-term forecasts of stocks
class ARIMAForecaster:
    def __init__(self, ticker) -> None:
        self.stockPrices = self.retrieveData(ticker)
        self.calculateReturns()
    
    # Retrives data from Yahoo Finance
    # Only need dates and adjusted close data
    def retrieveData(self, ticker):
        stockPrices = yf.download(ticker, start="2010-01-01")
        stockPrices = stockPrices.dropna()
        stockPrices = stockPrices.reset_index()
        stockPrices = stockPrices.rename(columns={"Date": "date", "Open": "open", "High": "high", "Low": "low", "Close": "close", "Adj Close": "adjClose", "Volume": "volume"})
        stockPrices = stockPrices.drop(columns=['open', 'high', 'low', 'close', 'volume'])
        
        return stockPrices
    
    # Obtains an approximation of percentage returns, contingent on the first-differenced series being stationary
    def calculateReturns(self):
        pass
        # TODO: Obtain returns
        # Constructing a new variable to achieve a stationary process.
        # Getting log difference approximation of percentage changes (a way of first differencing the data)
        self.stockPrices['logAdjClose'] = np.log(self.stockPrices['adjClose'])
        self.stockPrices['logDifAdjClose'] = self.stockPrices['logAdjClose'].diff()

        # Dropping first row as it does not have a percentage change
        self.stockPrices = self.stockPrices.dropna()
        # TODO: Test for stationarity of returns data, early return if it is not stationary (should be stationary considering financial theory)
        
    # Tests if the process is stationary
    def isStationaryProcess(self):
        pass
    
    # Higher-level method to abstract model creation (for the user to call)
    def createModel(self):
        p, q = self.obtainARIMAParameters()
        
        # Have already differenced the data and verified stationarity, so I do not need to difference data more
        self.model = self.constructARIMA(p, 0, q)
        
        print(self.model.summary())
        
    # Obtains optimal p and q fit values for ARIMA model using information criteria
    def obtainARIMAParameters(self):        
        acfResults = tsa.acf(self.stockPrices['logDifAdjClose'], alpha=0.05)
        pacfResults = tsa.pacf(self.stockPrices['logDifAdjClose'], alpha=0.05)
        
        
        # TODO: Replace this with an IC based selection of criteria
        # Will probably need to test residuals
        # Reference this: https://www.geeksforgeeks.org/box-jenkins-methodology-for-arima-models/
        return 2,2

    
    # Creates an ARIMA model with the provided p, d and q model
    def constructARIMA(self, p, d, q):
        return arima.ARIMA(endog=self.stockPrices['logDifAdjClose'], order=(p, 0, q)).fit()
    
    # Creates s-step ahead forecasts with the given model
    def getForecasts(self, s):

        finalDate = self.getFinalRealizedDate()
        stockForecastDates = []
        stockReturnForecasts = self.model.forecast(s)

        for i in range(1, len(stockReturnForecasts) + 1):
            stockForecastDates.append(finalDate + pd.DateOffset(days=i))

        stockReturnForecasts = pd.DataFrame({'date': stockForecastDates, 'logDifAdjClose': stockReturnForecasts})
        stockReturnForecasts = stockReturnForecasts.reset_index(drop=True)

        return stockReturnForecasts
    
    # Gets combined forecasted and realized returns
    def getCombinedReturns(self, s):
        stockReturnsWithForecasts = pd.DataFrame(self.stockPrices, columns=['date', 'logDifAdjClose'])

        # Add Dates to Forecasted date
        # Obtain final in-sample date
        finalDate = self.getFinalRealizedDate()
        
        stockReturnForecasts = forecaster.getForecasts(s)
        
        stockReturnsWithForecasts = pd.concat([stockReturnsWithForecasts, stockReturnForecasts])
        stockReturnsWithForecasts = stockReturnsWithForecasts.reset_index(drop=True)
        
        stockReturnsWithForecasts = stockReturnsWithForecasts.rename(columns={'logDifAdjClose': 'approxDailyReturn'})
        
        return stockReturnsWithForecasts
        
    # Get final date of recorded returns
    def getFinalRealizedDate(self):
        return self.stockPrices.iloc[len(self.stockPrices) - 1]['date']
        
# Class manual testing code
if __name__ == "__main__":
    forecaster = ARIMAForecaster("C")
    forecaster.createModel()
    stockReturnsWithForecasts = forecaster.getCombinedReturns(15)
    
    print(stockReturnsWithForecasts)