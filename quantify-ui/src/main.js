import { createApp } from 'vue'
import App from './App.vue'
import '../styles/app.css'
import SimpleTypeahead from 'vue3-simple-typeahead';
import 'vue3-simple-typeahead/dist/vue3-simple-typeahead.css';
import NavHeader from './components/NavHeader.vue'
import StockForm from './components/StockForm.vue';
import LSTMDetails from './components/LSTMDetails.vue';
import StockDetail from './components/StockDetail.vue';
import ForecastedReturnsTable from './components/ForecastedReturnsTable.vue';
import ReturnsGraph from './components/ReturnsGraph.vue';
import ARIMADetails from './components/ARIMADetails.vue';
import StockPriceGraph from './components/StockPriceGraph.vue'
import PrimeVue from 'primevue/config';
import Lara from '@primevue/themes/lara';
import SelectButton from 'primevue/selectbutton';
import DatePicker from 'primevue/datepicker'
import InputNumber from 'primevue/inputnumber'
import Divider from 'primevue/divider';
import Button from 'primevue/button';
import ProgressSpinner from 'primevue/progressspinner';
import Splitter from 'primevue/splitter';
import SplitterPanel from 'primevue/splitterpanel';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';

const app = createApp(App)

// Global registration
app.component('NavHeader', NavHeader);
app.component('StockForm', StockForm);
app.component('LSTMDetails', LSTMDetails);
app.component('StockDetail', StockDetail);
app.component('ForecastedReturnsTable', ForecastedReturnsTable);
app.component('ReturnsGraph', ReturnsGraph);
app.component('ARIMADetails', ARIMADetails);
app.component('StockPriceGraph', StockPriceGraph);

app.use(SimpleTypeahead);
app.use(PrimeVue, {
    theme: {
        preset: Lara
    }
});

app.component('SelectButton', SelectButton);
app.component('PrimeButton', Button);
app.component('DatePicker', DatePicker)
app.component('InputNumber', InputNumber)
app.component('Divider', Divider)
app.component('ProgressSpinner', ProgressSpinner)
app.component('Splitter', Splitter)
app.component('SplitterPanel', SplitterPanel)
app.component('DataTable', DataTable)
app.component('Column', Column)

app.mount('#app')