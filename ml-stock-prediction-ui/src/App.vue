<script setup>
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
<script>
import { Line } from 'vue-chartjs';
import {Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend} from 'chart.js'
import * as chartConfig from './chartConfig.js'

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
)

export default {
  name: 'App',
  components: {
    Line
  },
  data() {
    return chartConfig
  }
}
</script>

<template>
  <header>
    <NavHeader/>
  </header>

  <main>
    <StockForm @request-model="handleRequestModel"></StockForm>
    <ModelInformation></ModelInformation>
  </main>

  <Line :data="data" :options="options" />
</template>