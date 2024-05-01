<script setup>
import { ref } from 'vue';

const ticker = ref('')
const props = defineProps(['onSubmit'])
const emit = defineEmits(['request-model'])

const handleSubmit = (event) => {
    emit('request-model', event, ticker.value)
}

</script>

<template>
    <h2>Enter Stock Information</h2>
    <form @submit.prevent="handleSubmit">
        <input v-model="ticker" placeholder="Ticker Symbol"/>
        <button>Create Model</button>
    </form>
</template>