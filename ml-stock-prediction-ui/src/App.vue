<script setup>
import NavHeader from './components/NavHeader.vue'
import StockForm from './components/StockForm.vue';
import ModelInformation from './components/ModelInformation.vue';
import axios from 'axios';

// Requests to create a ML model from the back-end
const handleRequestModel = (event, inputTicker, inputForecastPeriod) =>{
    // FIXME: Remove specific IP and port specification
    axios.post("http://127.0.0.1:8000/arimaForecast/", {
      ticker: inputTicker,
      forecastLength: inputForecastPeriod
    })
    .then(response => (alert(response.data)))
    .catch(e => alert(e))

}
</script>

<template>
  <header>
    <NavHeader></NavHeader>
  </header>

  <main>
    <StockForm @request-model="handleRequestModel"></StockForm>
    <ModelInformation></ModelInformation>
  </main>
</template>