<script setup>
import { ref } from 'vue';

let ticker = ref('')
</script>

<template>
    <h2>Enter Stock Information</h2>
    <form>
        <input v-model="ticker" placeholder="Ticker Symbol"/>
        <button>Create Model</button>
    </form>
</template>