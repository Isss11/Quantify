<script setup>
import {Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend} from 'chart.js'
import { Line } from 'vue-chartjs'

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip,Legend)

const props = defineProps({parameters: Object, details: Object, prices: Object});

const getDataRealized = () => {
  return {
  labels: getCombinedDates(),
  datasets: [
    {
      label: "Adjusted Close Prices ('Realized')",
      backgroundColor: getPointColours(),
      data: getCombinedPrices(),
    },
  ]
  }
}

// Chooses different colours for realized vs forecasted points
const getPointColours = (pointInfo) => {
  const pointColours = []
  const realizedColour = '#23cbed'
  const forecastedColour = '#eda323'

  for (let i = 0; i < props.prices.realized.prices.length; ++i) {
    pointColours.push(realizedColour)
  }

  for (let i = 0; i < props.prices.forecasted.prices.length; ++i) {
    pointColours.push(forecastedColour)
  }

  return pointColours
}

const getCombinedDates = () => {
  console.log('combined dates', [...props.prices.realized.date, ...props.prices.forecasted.date])

  return [...props.prices.realized.date, ...props.prices.forecasted.date]
}

const getCombinedPrices = () => {
  return [...props.prices.realized.prices, ...props.prices.forecasted.prices]
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