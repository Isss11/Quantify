<script setup>
    const props = defineProps(['returns', 'ticker', 'forecastLength'])
</script>

<template>
    <h2>Model Information</h2>
    <ReturnsGraph :realized="props.returns.realized" :forecasted="props.returns.forecasted" :ticker="props.ticker" :forecastLength="props.forecastLength"/>
</template>