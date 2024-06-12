<script setup>
import {Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title,Tooltip,Legend} from 'chart.js'
import { Line } from 'vue-chartjs'

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip,Legend)

const props = defineProps({parameters: Object, details: Object, prices: Object});

console.log({props})

const getDataRealized = () => {
  return {
  labels: props.prices.realized.date,
  datasets: [
    {
      label: props.ticker + "Adjusted Close Prices",
      backgroundColor: '#f87979',
      data: props.prices.realized.prices,
    }
  ]
  }
}

const getOptionsRealized = () => {
  return {
    scales: {
    }
  }
}
</script>

<template>
    <h3>Prices (realized and forecasted)</h3>
    <Line :data="getDataRealized()" :options="getOptionsRealized()"/>
</template>