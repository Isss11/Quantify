import pandas as pd
import yfinance as yf
import json

# Class that returns basic stock information about the selected stock
class StockDetail:
    def __init__(self, ticker) -> None:
        self.stock = yf.Ticker(ticker).info
        
    # Returning relevant information from Yahoo Finance API
    def getGeneralInfo(self):
        generalInfo = dict()
        generalInfo["tickerSymbol"] = self.stock['underlyingSymbol']
        generalInfo["name"] = self.stock["shortName"]
        generalInfo["exchange"] = self.stock["exchange"]
        generalInfo["low"] = self.stock["fiftyTwoWeekLow"]
        generalInfo["high"] = self.stock["fiftyTwoWeekHigh"]
        generalInfo["description"] = self.stock["longBusinessSummary"]
        
        return generalInfo
        
if __name__ == "__main__":
    stock = StockDetail("C")
    print(stock.getGeneralInfo())