<script setup>
    const props = defineProps(['ticker', 'companyName', 'price', 'low', 'high', ])
</script>

<template>
    <span>
        <h3>{{props.companyName}} ({{ props.ticker }})</h3>
        <h4>{{ props.price }} USD</h4>
    </span>


</template>