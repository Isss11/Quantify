<script setup>
    const props = defineProps(['ticker', 'companyName', 'price', 'currency' ])
</script>

<template>
    <span v-if="props.ticker">
        <h3>{{props.companyName}} ({{ props.ticker }})</h3>
        <h4>{{ props.price }} {{props.currency}}</h4>
    </span>
</template>