import pandas as pd

def getTickers():
    stocks = pd.read_csv('valid_tickers.csv')
    
    return stocks['stockName'].tolist()

if __name__ == '__main__':
    print(getTickers())