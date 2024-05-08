<script setup>
import { ref } from 'vue';

const props = defineProps(['realized', 'forecasted', 'ticker', 'forecastLength']);

const dataRealized = {
  labels: props.realized.date,
  datasets: [
    {
      label: props.ticker + " Approx. Returns (%)",
      backgroundColor: '#f87979',
      data: props.realized.returns,
    }
  ]
}

const dataForecasted = {
  labels: props.forecasted.date,
  datasets: [
    {
      label: props.ticker + " Approx. Returns (%)",
      backgroundColor: '#e81481',
      data: props.forecasted.returns,
    }
  ]
}
</script>

<script>
import {Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title,Tooltip,Legend} from 'chart.js'
import { ref } from 'vue';
import { Line } from 'vue-chartjs'

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip,Legend)
</script>

<template>
    <h3>Realized Returns (approximated)</h3>
    <Line :data="dataRealized"/>
    <h3>Forecasted Returns ({{ props.forecastLength }}-day forecast, approximated)</h3>
    <Line :data="dataForecasted"/>
</template>