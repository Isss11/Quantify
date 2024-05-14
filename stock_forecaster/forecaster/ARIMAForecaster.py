import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.tsa.stattools as tsa
import statsmodels.tsa.arima.model as arima
import statsmodels.graphics.tsaplots as tsaPlots
import pmdarima as pm
import yfinance as yf

# Uses Auto-regressive Integrated Moving Average Model to perform short-term forecasts of stocks
class ARIMAForecaster:
    def __init__(self, ticker, sampleStartDate) -> None:
        self.stockPrices = self.retrieveData(ticker, sampleStartDate)
        self.calculateReturns()
    
    # Retrives data from Yahoo Finance
    # Only need dates and adjusted close data
    def retrieveData(self, ticker, sampleStartDate):
        stockPrices = yf.download(ticker, start=sampleStartDate)
        stockPrices = stockPrices.dropna()
        stockPrices = stockPrices.reset_index()
        stockPrices = stockPrices.rename(columns={"Date": "date", "Open": "open", "High": "high", "Low": "low", "Close": "close", "Adj Close": "adjClose", "Volume": "volume"})
        stockPrices = stockPrices.drop(columns=['open', 'high', 'low', 'close', 'volume'])
        
        return stockPrices
    
    # Obtains an approximation of percentage returns, contingent on the first-differenced series being stationary
    def calculateReturns(self):
        # Constructing a new variable to achieve a stationary process.
        # Getting log difference approximation of percentage changes (a way of first differencing the data)
        self.stockPrices['logAdjClose'] = np.log(self.stockPrices['adjClose'])
        self.stockPrices['logDifAdjClose'] = self.stockPrices['logAdjClose'].diff()
        
        # Convert to percentage changes (and drop top row since it does not have a percentage change)
        self.stockPrices = self.stockPrices.dropna()
        self.stockPrices['logDifAdjClose'] = self.stockPrices['logDifAdjClose'] * 100
        
    # TODO: Ensures differenced process is stationary.
    def isStationaryProcess(self):
        pass
    
    # Higher-level method to abstract model creation (for the user to call)
    def createModel(self):
        p, d, q = self.obtainARIMAParameters()
        
        # TODO: thow an exception
        if d > 0:
            print("An error has occurred. Returns are non-stationary.")
            return
        
        # Have already differenced the data and verified stationarity, so I do not need to difference data more
        self.model = arima.ARIMA(endog=self.stockPrices['logDifAdjClose'], order=(p, 0, q)).fit()
        
        print(self.model.summary())
        
        return self.getModelDetails()
    
    # Extracts the model details from the current model summary
    def getModelDetails(self):
        modelSummary = pd.read_html(self.model.summary().tables[1].as_html(), header=0)[0]
        modelSummary = modelSummary.rename(columns={'std err': 'stdErr', 'P>|z|': 'p', 'coef': 'coefficient', '[0.025': 'lowerBound', '0.975]': 'upperBound', 'Unnamed: 0': 'estimator'})
        
        # Convert Model Summary to a Dictionary for the FE
        modelDetails = []
        for i in range(modelSummary.shape[0]):
            modelDetails.append(modelSummary.iloc[i].to_dict())
        
        return modelDetails
        
    # Obtains optimal p and q fit values for ARIMA model using information criteria
    def obtainARIMAParameters(self):        
        # Using auto_arima from a different package to optain optimal p and q
        autoARIMAModel = pm.auto_arima(self.stockPrices['logDifAdjClose'], start_p=1, start_q=1, test='adf', max_p=30, max_q=30, information_criterion='aic', stepwise=True)
        
        return autoARIMAModel.order[0], autoARIMAModel.order[1], autoARIMAModel.order[2]
    
    # Creates s-step ahead forecasts with the given model
    def getForecasts(self, s):

        finalDate = self.getFinalRealizedDate()
        stockForecastDates = []
        stockReturnForecasts = self.model.forecast(s)

        # FIXME: Adjust for weekends
        for i in range(1, len(stockReturnForecasts) + 1):
            stockForecastDates.append(finalDate + pd.DateOffset(days=i))

        stockReturnForecasts = pd.DataFrame({'date': stockForecastDates, 'logDifAdjClose': stockReturnForecasts})
        stockReturnForecasts = stockReturnForecasts.reset_index(drop=True)

        return stockReturnForecasts
    
    # Gets combined forecasted and realized returns
    def getReturns(self, s):
        realizedStockReturns = pd.DataFrame(self.stockPrices, columns=['date', 'logDifAdjClose'])
        realizedStockReturns = realizedStockReturns.rename(columns={'logDifAdjClose': 'approxDailyReturn'})
        
        forecastedStockReturns = self.getForecasts(s)
        forecastedStockReturns = forecastedStockReturns.rename(columns={'logDifAdjClose': 'approxDailyReturn'})
        
        # Remove time from date columns
        realizedStockReturns['date'] = realizedStockReturns['date'].dt.date
        forecastedStockReturns['date'] = forecastedStockReturns['date'].dt.date
        
        # Organize data into a dictionary to be consumed
        stockReturns = {'realized': {'date': realizedStockReturns['date'].tolist(), 'returns': realizedStockReturns['approxDailyReturn'].tolist()},
                        'forecasted': {'date': forecastedStockReturns['date'].tolist(), 'returns': forecastedStockReturns['approxDailyReturn'].tolist()}}
        
        return stockReturns
        
    # Get final date of recorded returns
    def getFinalRealizedDate(self):
        return self.stockPrices.iloc[len(self.stockPrices) - 1]['date']
        
# Class manual testing code
if __name__ == "__main__":
    forecaster = ARIMAForecaster("AAPL")
    modelDetails = forecaster.createModel()
    print(modelDetails)
    # stockReturnsWithForecasts = forecaster.getReturns(5)
    # print(stockReturnsWithForecasts)