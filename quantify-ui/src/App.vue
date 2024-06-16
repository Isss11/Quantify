<script setup>
import axios from 'axios';
import { ref } from 'vue';
import '../styles/app.css'

const modelParameters = ref('')
const modelDetails = ref('')
const modelPrices = ref('');
const modelAccuracy = ref('')
const modelExists = ref(false);

// Requests to forecast stock returns using an ARIMA model
const handleRequestModel = (e, inputTicker, inputForecastPeriod, chosenModel, startDate, lookBack, epochs, batchSize) => {
  // ARIMA Model
  if (chosenModel === 'arima') {
    // axios.post("http://127.0.0.1:8000/arimaForecast/", {
    //   ticker: inputTicker, 
    //   forecastLength: inputForecastPeriod,
    //   sampleStartDate: startDate
    // })
    //   .then(response => {
    //     // An empty object is truthy, so boolean ref was created to denote whether the model information component should be rendered or not
    //     modelReturns.value = response.data;
    //     modelExists.value = true;
    //     ticker.value = inputTicker;
    //     forecastPeriod.value = inputForecastPeriod;

    //     console.log("Realized and Forecasted Values (ARIMA): ", modelReturns.value);
    //   })
    //   .catch(e => alert(e))
  } else {
    axios.post("http://127.0.0.1:8000/lstmForecast/", {
      ticker: inputTicker,
      forecastLength: inputForecastPeriod,
      sampleStartDate: startDate,
      lookBack: 8,
      epochs: 3,
      batchSize: 1
    })
    .then(response => {
      modelParameters.value = response.data.parameters,
      modelDetails.value = response.data.details,
      modelPrices.value = response.data.prices
      modelAccuracy.value = response.data.modelAccuracy

      // Indicate that the model exists to show the model display
      modelExists.value = true;
    })
  }
}
</script>

<template>
  <header>
    <NavHeader />
  </header>
  <main class="main-panel">
      <div class="form-column">
        <StockForm @request-model="handleRequestModel" />
      </div>
      <div class="model-graph-column">
        <Model v-if="modelExists" :parameters="modelParameters" :details="modelDetails" :prices="modelPrices" :accuracy="modelAccuracy"/>
      </div>
  </main>
</template>