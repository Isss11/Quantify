<script setup>
const props = defineProps({parameters: Object, details: Object, prices: Object, accuracy: Object})

console.log('props value', props.parameters);

</script>

<template>
    <h2>Model</h2>
    <StockPriceGraph :parameters="parameters" :details="details" :prices="prices"/>
</template>