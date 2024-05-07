<script setup>

const data = {
  labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
  datasets: [
    {
      label: 'Data One',
      backgroundColor: '#000000',
      data: [40, 39, 10, 40, 39, 80, 40]
    }
  ]
}

const options = {
  responsive: true,
  maintainAspectRatio: false
}

</script>

<template>
    <h3>Returns (Realized and Forecasted)</h3>
    <Line :data="data" :options="options"/>
    <div>Graph above</div>
</template>