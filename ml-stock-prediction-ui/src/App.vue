<script setup>
import NavHeader from './components/NavHeader.vue'
import StockForm from './components/StockForm.vue';
import ModelInformation from './components/ModelInformation.vue';

// Requests to create a ML model from the back-end
const handleRequestModel = (event, value) =>{
    alert("From the child:" + value)
}
</script>

<template>
  <header>
    <NavHeader></NavHeader>
  </header>

  <main>
    <StockForm @request-model="handleRequestModel"></StockForm>
    <ModelInformation></ModelInformation>
  </main>
</template>