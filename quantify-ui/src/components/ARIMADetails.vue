<script setup>
const props = defineProps(['modelDetails'])
// console.log("Model Details: ", props.modelDetails['std err']);
</script>

<template>
    <h3>Model Details (SARIMA)</h3>
    <table>
        <tr>
            <th>Estimator</th>
            <th>Coefficient</th>
            <th>Standard Error</th>
            <th>Test Statistic (z)</th>
            <th>P > |z|</th>
            <th>Lower-bound (0.025)</th>
            <th>Upper-bound (0.975)</th>
        </tr>
        <tr v-for="detail in modelDetails">
            <td>{{ detail.estimator }}</td>
            <td>{{ detail.coefficient }}</td>
            <td>{{ detail.stdErr }}</td>
            <td>{{ detail.z }}</td>
            <td>{{ detail.p }}</td>
            <td>{{ detail.lowerBound }}</td>
            <td>{{ detail.upperBound }}</td>
        </tr>
    </table>
</template>