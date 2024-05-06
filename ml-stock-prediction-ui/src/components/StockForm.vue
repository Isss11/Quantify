<script setup>
import { ref } from 'vue';
import { onMounted } from 'vue';
import axios from 'axios';
import validTickers from '@/assets/validTickers';

const ticker = ref('')
const forecastPeriod = ref('')
const props = defineProps(['onSubmit'])
const emit = defineEmits(['request-model'])

const handleSubmit = (event) => {
    emit('request-model', event, ticker.value, forecastPeriod.value)
}
</script>

<template>
    <h2>Enter Stock Information</h2>
    <form @submit.prevent="handleSubmit">
        <vue3-simple-typeahead 
            id="tickerSelector"
            :items="validTickers"
            :minInputLength="1"
        />
        <input type="number" min="1" v-model="forecastPeriod" placeholder="Forecast Period"/>
        <button>Forecast</button>
    </form>
</template>