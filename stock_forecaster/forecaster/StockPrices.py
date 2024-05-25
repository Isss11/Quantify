import yfinance as yf
import numpy as np
import pandas as pd

class StockPrices:
    def __init__(self, ticker, sampleStartDate) -> None:
        self.prices = self.retrieveData(ticker, sampleStartDate)
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
        self.prices['logAdjClose'] = np.log(self.prices['adjClose'])
        self.prices['logDifAdjClose'] = self.prices['logAdjClose'].diff()
        
        # Convert to percentage changes (and drop top row since it does not have a percentage change)
        self.prices = self.prices.dropna()
        self.prices['logDifAdjClose'] = self.prices['logDifAdjClose'] * 100
        
    # Get final date of recorded returns
    def getFinalRealizedDate(self):
        return self.prices.iloc[len(self.prices) - 1]['date']