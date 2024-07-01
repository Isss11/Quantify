<script setup>
import { computed } from 'vue';

const props = defineProps(['details', 'parameters'])
const adjustedDetails = computed(() => {
    const adjustedDetails = [{'train': Number(props.details.rsme.train.toFixed(2)), 'test': Number(props.details.rsme.test.toFixed(2))}]

    return adjustedDetails
})
</script>

<template>
    <h2>Model</h2>
    <h3>Details</h3>
    <h3>Accuracy (RSME)</h3>


    <DataTable :value="adjustedDetails">
        <Column field="train" header="Train"></Column>
        <Column field="test" header="Test"></Column>
    </DataTable>
</template>