<script setup>
import { ref } from 'vue';
import NavHeader from './components/NavHeader.vue'
import StockForm from './components/StockForm.vue';
import ModelInformation from './components/ModelInformation.vue';

// Requests to create a ML model from the back-end
const handleRequestModel = (event, value) =>{
    alert("From the child:" + value)
}

const ticker = ref('')
</script>

<template>
  <header>
    <NavHeader></NavHeader>
  </header>

  <main>
    <StockForm @request-model="handleRequestModel"></StockForm>
    <ModelInformation></ModelInformation>
    {{ticker}}
  </main>
</template>