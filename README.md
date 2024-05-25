# Quantify

_This project is currently being worked on, and is not finished_.

## Set-up

### Front-end

1. Change into the `quantify-ui` directory and install dependencies.

```
cd quantify-ui
```

```
npm install
```

2. Run the front-end application.

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

_Will list acknowledgements here, if needed._

1. For valid tickers file: https://github.com/ahnazary/Finance/blob/master/finance/src/database/valid_tickers.csv
2. For LSTM model code: https://www.youtube.com/watch?v=CbTU92pbDKw&t.
