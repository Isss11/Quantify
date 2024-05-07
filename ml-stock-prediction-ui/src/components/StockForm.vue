<script setup>
import { ref } from 'vue';
import axios from 'axios';
import validTickers from '@/assets/validTickers';
import StockDetail from './StockDetail.vue';

const ticker = ref('')
const forecastPeriod = ref('')
const stockDetails = ref({})
const props = defineProps(['onSubmit'])
const emit = defineEmits(['request-model'])

const handleSubmit = (e) => {
    emit('request-model', e, ticker.value, forecastPeriod.value)
}

const handleChange = (e) => {
    axios.post("http://127.0.0.1:8000/stockDetail/" + e + "/")
    .then(response => {
        ticker.value = e;
        stockDetails.value = response.data;
        console.log(ticker.value)
        console.log(stockDetails.value.name)
    })
    .catch(e => alert("Stock not available for forecasting."))
}
</script>

<template>
    <h2>Enter Stock Information</h2>
    <form @submit.prevent="handleSubmit">
        <vue3-simple-typeahead
            id="tickerSelector"
            placeholder="Stock Ticker"
            :items="validTickers"
            @selectItem="handleChange"
        />
        <input type="number" min="1" v-model="forecastPeriod" placeholder="Forecast Period"/>
        <button>Forecast</button>
        <StockDetail :ticker="ticker" :companyName="stockDetails.name" :price="stockDetails.price"</StockDetail>
    </form>
</template>