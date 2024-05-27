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
        self.lookBack = lookBack
        
        self.normalizedPrices = self.stock.getNormalizedData(self.scaler)
        
        # Create training and test data for model evaluation
        # Actual predictions (indicated in the app's UI) will be for data beyond current date
        trainSize = int(len(self.normalizedPrices) * 0.7)
        # testSize = len(self.normalizedPrices) - trainSize
        
        trainingData = self.normalizedPrices[0:trainSize,:]
        testData = self.normalizedPrices[trainSize:len(self.normalizedPrices),:]
        
        # Create data-set with a given look-back amount
        self.trainX, self.trainY = self.createDataset(trainingData, self.lookBack)
        self.testX, self.testY = self.createDataset(testData, self.lookBack)
        
        # Reshape data to fit with model
        self.trainX = np.reshape(self.trainX, (self.trainX.shape[0], 1, self.trainX.shape[1]))
        self.testX = np.reshape(self.testX, (self.testX.shape[0], 1, self.testX.shape[1]))
        
        # TODO, make the number of Epocs a parameter
        self.model = self.getLSTM(self.trainX, self.trainY, 1)
        
    def getLSTM(self, trainX, trainY, numEpochs):
        model = Sequential()
        model.add(LSTM(4, input_shape=(1, self.lookBack)))

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
        trainPredicted = self.makeForecasts(self.trainX)
        testPredicted = self.makeForecasts(self.testX)
        
        trainActual = self.scaler.inverse_transform([self.trainY])
        testActual = self.scaler.inverse_transform([self.testY])
        
        trainScore = self.computeError(trainPredicted, trainActual)
        testScore = self.computeError(testPredicted, testActual)
        
        return trainScore, testScore
        
    def computeError(self, predicted, actual):
        return np.sqrt(mean_squared_error(actual[0], predicted[:,0]))
    
    # Develops Forecasts
    def makeForecasts(self, X):
        print("Making forecasts with X")
        print(X.shape)
        print(X)
        predictions = self.model.predict(X)
        
        # Change predictions back to original units to calculate RMSE in original units
        return self.scaler.inverse_transform(predictions)
        
    # For returning the final predictions, along with their actual values
    def getCombinedPrices(self):
        pass
    
    def predictIntoFuture(self, s):
        predictionList = self.normalizedPrices[-self.lookBack:]

        # For forecasted values only
        predictedNormalizedPrices = []

        # Using look-back amount to append to normalized dataset and using forecasted data to predict future forecasted values
        # Note that this will cause larger errors, but is needed to perform real forecasts
        for day in range(s):
            # Merging together the predicted and actual prices to use in future forecasts, if there are some predictions made
            if len(predictedNormalizedPrices) != 0:
                npPredicted = np.reshape(np.array(predictedNormalizedPrices), (-1, 1))    
                combinedPrices = np.concatenate((self.normalizedPrices, npPredicted))
            else:
                combinedPrices = self.normalizedPrices
            
            # Taking the past amount of values, specified by the lookback amount. This will be used in the model predictions.
            X = np.reshape(combinedPrices[-self.lookBack:], (-1, 1, self.lookBack))
            
            # Obtaining predicted price and adding it to the predicted prices array to be used in future forecasts (depending on lookback amount)
            predictedPrice = self.model.predict(X)[0][0]
            
            predictedNormalizedPrices.append(predictedPrice)
            
        predictedPrices = self.scaler.inverse_transform(np.reshape(predictedNormalizedPrices, (-1, 1)))
            
        return predictedPrices
        
# Class manual testing code
if __name__ == "__main__":
    forecaster = LSTMForecaster("C", "2010-01-01")
    forecaster.createModel(8)
    print(forecaster.measureModelAccuracy())

    # Forecast in the future (beyond the training and sample data
    print("Obtaining predictions")
    print(forecaster.predictIntoFuture(20))