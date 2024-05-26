import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import yfinance as yf
from StockPrices import StockPrices

# Uses an LSTM model to forecast prices of a given stock
class LSTMForecaster:
    def __init__(self, ticker, sampleStartDate) -> None:
        self.stock = StockPrices(ticker, sampleStartDate)
        self.scaler = MinMaxScaler(feature_range=(0, 1))
        
        print(self.stock.prices)
        
    # Creates LSTM Model
    def createModel(self, lookBack):
        normalizedPrices = self.stock.getNormalizedData(self.scaler)
        
        # Create training and test data for model evaluation
        # Actual predictions (indicated in the app's UI) will be for data beyond current date
        trainSize = int(len(normalizedPrices) * 0.7)
        # testSize = len(normalizedPrices) - trainSize
        
        trainingData = normalizedPrices[0:trainSize,:]
        testData = normalizedPrices[trainSize:len(normalizedPrices),:]
        
        # Create data-set with a given look-back amount
        self.trainX, self.trainY = self.createDataset(trainingData, lookBack)
        self.testX, self.testY = self.createDataset(testData, lookBack)
        
        # Reshape data to fit with model
        self.trainX = np.reshape(self.trainX, (self.trainX.shape[0], 1, self.trainX.shape[1]))
        self.testX = np.reshape(self.testX, (self.testX.shape[0], 1, self.testX.shape[1]))
        
        self.model = self.getLSTM(lookBack, self.trainX, self.trainY, 3)
        
    def getLSTM(self, lookBack, trainX, trainY, numEpochs):
        model = Sequential()
        model.add(LSTM(4, input_shape=(1, lookBack)))

        # Adds a neural network layer with one input
        model.add(Dense(1))

        model.compile(loss='mean_squared_error', optimizer='adam')
        model.fit(trainX, trainY, epochs=numEpochs, batch_size=1, verbose=2)
        
        return model
        
    # Source: https://machinelearningmastery.com/time-series-prediction-lstm-recurrent-neural-networks-python-keras/
    def createDataset(self, dataset, lookBack):
        dataX, dataY = [], []
    
        for i in range(len(dataset)-lookBack-1):
            a = dataset[i:(i + lookBack), 0]
            dataX.append(a)
            dataY.append(dataset[i + lookBack, 0])

        return np.array(dataX), np.array(dataY)
    
    # Analyzes quality of model, comparing the results of the training data and test data
    def measureModelAccuracy(self):
        trainPredicted, trainActual = self.makeForecasts(self.trainX, self.trainY)
        testPredicted, testActual = self.makeForecasts(self.testX, self.testY)
        
        trainScore = self.computeError(trainPredicted, trainActual)
        testScore = self.computeError(testPredicted, testActual)
        
        return trainScore, testScore
        
    def computeError(self, predicted, actual):
        return np.sqrt(mean_squared_error(actual[0], predicted[:,0]))
    
    # Develops Forecasts
    def makeForecasts(self, X, y):
        predictions = self.model.predict(X)
        
        # Change predictions back to original units to calculate RMSE in original units
        predictionsTransformed = self.scaler.inverse_transform(predictions)
        yTransformed = self.scaler.inverse_transform([y])
        
        return predictionsTransformed, yTransformed
    
    # For returning the final predictions, along with their actual values
    def getCombinedPrices(self):
        pass
    
        
# Class manual testing code
if __name__ == "__main__":
    forecaster = LSTMForecaster("AAPL", "2010-01-01")
    forecaster.createModel(8)
    print(forecaster.measureModelAccuracy())
    # print(modelDetails)
    # stockReturnsWithForecasts = forecaster.getCombinedReturns(5)
    # print(stockReturnsWithForecasts)