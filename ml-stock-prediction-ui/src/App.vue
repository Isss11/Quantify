<script setup>
import axios from 'axios';
import { ref } from 'vue';

const modelReturns = ref();
const modelExists = ref(false);
const ticker = ref('');
const forecastPeriod = ref('');


// Requests to forecast stock returns using an ARIMA model
const handleRequestModel = (e, inputTicker, inputForecastPeriod, chosenModel, startDate) => {
  // ARIMA Model
  if (chosenModel === 'arima') {
    axios.post("http://127.0.0.1:8000/arimaForecast/", {
      ticker: inputTicker,
      forecastLength: inputForecastPeriod,
      sampleStartDate: startDate
    })
      .then(response => {
        // An empty object is truthy, so boolean ref was created to denote whether the model information component should be rendered or not
        modelReturns.value = response.data;
        modelExists.value = true;
        ticker.value = inputTicker;
        forecastPeriod.value = inputForecastPeriod;

        console.log("Realized and Forecasted Values (ARIMA): ", modelReturns.value);
      })
      .catch(e => alert(e))
    // TODO: ML Model
  } else {

  }
}
</script>

<template>
  <header>
    <NavHeader />
  </header>

  <main>
    <StockForm @request-model="handleRequestModel" />
    <Model v-if="modelExists" :returns="modelReturns" :ticker="ticker" :forecastLength="forecastPeriod" />
  </main>
</template>