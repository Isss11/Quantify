<script setup>
const props = defineProps(['returns', 'ticker', 'forecastLength'])
</script>

<template>
    <h2>Model</h2>
    <ARIMADetails :modelDetails="props.returns.modelDetails" />
    <ReturnsGraph :realized="props.returns.realized" :forecasted="props.returns.forecasted" :ticker="props.ticker"
        :forecastLength="props.forecastLength" />
</template>