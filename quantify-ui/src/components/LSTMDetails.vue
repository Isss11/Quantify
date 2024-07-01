<script setup>
import { computed } from 'vue';

const props = defineProps({details: Object, parameters: Object})
</script>

<template>
    <h2>Model</h2>
    <h3>Details</h3>
    <h3>Accuracy (RSME)</h3>


    <DataTable :value="details">
        <Column field="train" header="Train"></Column>
        <Column field="test" header="Test"></Column>
    </DataTable>
</template>