<script setup>
import { ref } from 'vue';
import axios from 'axios';
import validTickers from '../assets/validTickers';
import SelectButton from 'primevue/selectbutton';
import InputNumber from 'primevue/inputnumber';

const ticker = ref('')
const forecastPeriod = ref('')
const stockDetails = ref({})
const chosenModel = ref('ARIMA')
const startDate = ref('2010-01-01')
const lookBack = ref('')
const epochs = ref('')
const batchSize = ref('')
const modelOptions = ref(['ARIMA', 'LSTM'])

const emit = defineEmits(['request-model'])

const handleSubmit = (e) => {
    emit('request-model', e, ticker.value, forecastPeriod.value, chosenModel.value, startDate.value, lookBack.value, epochs.value, batchSize.value)
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

        <StockDetail :ticker="ticker" :companyName="stockDetails.name" :price="stockDetails.price" :currency="stockDetails.currency"/>

        <SelectButton v-model="chosenModel" :options="modelOptions"/>
        <DatePicker v-model="startDate"/>
        <InputNumber :min="1" v-model="forecastPeriod" placeholder="Forecast Period"/>
        <InputNumber :min="1" v-model="lookBack" placeholder="Lookback"/>
        <InputNumber :min="1" v-model="epochs" placeholder="Epochs"/>
        <InputNumber :min="1" v-model="batchSize" placeholder="Batch Size"/>

        <PrimeButton label="Forecast"/>

    </form>
</template>