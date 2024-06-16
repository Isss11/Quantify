<script setup>
import { ref } from 'vue';
import axios from 'axios';
import validTickers from '../assets/validTickers';

const ticker = ref('')
const forecastPeriod = ref(null)
const stockDetails = ref({})
const chosenModel = ref('ARIMA')
const startDate = ref('2010-01-01')
const lookBack = ref(null)
const epochs = ref(null)
const batchSize = ref(null)
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


    <form>
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

        <label for="forecastInput">Forecast Length</label>
        <InputNumber id="forecastInput" :min="1" v-model="forecastPeriod"/>

        <div v-if="chosenModel === 'LSTM'">
        <Divider/>
        <h4>LSTM Parameters</h4>
        <label for="lookBackLength">Look Back Length</label>
        <InputNumber id="lookbackLength" :min="1" :max="30" v-model="lookBack"/>
        <label for="epochsInput">Epochs</label>
        <InputNumber id="epochsInput" :min="1" :max="5" v-model="epochs"/>
        <label for="batchSizeInput">Batch Size</label>
        <InputNumber id="batchSizeInput" :min="1" :max="30" v-model="batchSize"/>
        </div>

        <PrimeButton label="Forecast" @click="handleSubmit"/>

    </form>
</template>