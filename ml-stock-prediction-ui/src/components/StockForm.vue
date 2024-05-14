<script setup>
import { ref, watch } from 'vue';
import axios from 'axios';
import validTickers from '@/assets/validTickers';

const ticker = ref('')
const forecastPeriod = ref('')
const stockDetails = ref({})
const chosenModel = ref('')
const startDate = ref('2010-01-01')
const emit = defineEmits(['request-model'])

const handleSubmit = (e) => {
    emit('request-model', e, ticker.value, forecastPeriod.value, chosenModel.value, startDate.value)
}

const handleChange = (e) => {
    axios.post("http://127.0.0.1:8000/stockDetail/" + e.input + "/")
    .then(response => {
        ticker.value = e.input;
        stockDetails.value = response.data;
    })
    .catch(e => console.log("Stock not available for forecasting."))
}
</script>

<template>
    <h2>Enter Stock Information</h2>
    <form @submit.prevent="handleSubmit">
        <vue3-simple-typeahead
            id="tickerSelector"
            placeholder="Stock Ticker"
            :items="validTickers"
            @onInput="handleChange"
            :minInputLength="1"
        />

        <input type="date" v-model="startDate" id="startDate" name="startDate"/>
        <input type="number" min="1" v-model="forecastPeriod" placeholder="Forecast Period"/>
        <StockDetail :ticker="ticker" :companyName="stockDetails.name" :price="stockDetails.price" :currency="stockDetails.currency"</StockDetail>

        <div>
            <label for="modelType">Model Type</label>
            <div id="modelType">
                <label for="arima">ARIMA</label>
                <input id="arima" type="radio" v-model="chosenModel" value="arima"/>
                <label for="ml">ML</label>
                <input id="ml" type="radio" v-model="chosenModel" value="ml"/>
            </div>  
        </div>

        <button>Forecast</button>

    </form>
</template>