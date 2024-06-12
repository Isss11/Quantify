# Quantify

_This project is currently being worked on_.

## Set-up

### Front-end

1. Change into the `quantify-ui` directory and install dependencies.

```
cd quantify-ui
```

```
npm install
```

2. Run the front-end application on **Google Chrome**.

```
npm run dev
```

### Back-end

1. Create a virtual environment to run the Django application in.

```
py -m venv stockPredictorEnv
```

2. Activate the virtual environment.

```
stockPredictorEnv\Scripts\activate
```

3. Use the terminal you activated the virtual environment, run the Django application.

```
cd stock_forecaster
```

```
py manage.py runserver
```

## Acknowledgments

1. For valid tickers file: https://github.com/ahnazary/Finance/blob/master/finance/src/database/valid_tickers.csv
2. https://www.youtube.com/watch?v=CbTU92pbDKw&t.
3. https://machinelearningmastery.com/time-series-prediction-lstm-recurrent-neural-networks-python-keras/
