import { createApp } from 'vue'
import App from './App.vue'
import SimpleTypeahead from 'vue3-simple-typeahead';
import 'vue3-simple-typeahead/dist/vue3-simple-typeahead.css';
import NavHeader from './components/NavHeader.vue'
import StockForm from './components/StockForm.vue';
import Model from './components/Model.vue';
import StockDetail from './components/StockDetail.vue';
import ForecastedReturnsTable from './components/ForecastedReturnsTable.vue';
import ReturnsGraph from './components/ReturnsGraph.vue';
import ARIMADetails from './components/ARIMADetails.vue';
import StockPriceGraph from './components/StockPriceGraph.vue'
import PrimeVue from 'primevue/config';
import Aura from '@primevue/themes/aura';
import SelectButton from 'primevue/selectbutton';
import DatePicker from 'primevue/datepicker'
import InputNumber from 'primevue/inputnumber'
import Divider from 'primevue/divider';
import Button from 'primevue/button';

const app = createApp(App)

// Global registration
app.component('NavHeader', NavHeader);
app.component('StockForm', StockForm);
app.component('Model', Model);
app.component('StockDetail', StockDetail);
app.component('ForecastedReturnsTable', ForecastedReturnsTable);
app.component('ReturnsGraph', ReturnsGraph);
app.component('ARIMADetails', ARIMADetails);
app.component('StockPriceGraph', StockPriceGraph);

app.use(SimpleTypeahead);
app.use(PrimeVue, {
    theme: {
        preset: Aura
    }
});

app.component('SelectButton', SelectButton);
app.component('PrimeButton', Button);
app.component('DatePicker', DatePicker)
app.component('InputNumber', InputNumber)
app.component('Divider', Divider)

app.mount('#app')