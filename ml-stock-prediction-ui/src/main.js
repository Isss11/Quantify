import { createApp } from 'vue'
import App from './App.vue'
import SimpleTypeahead from 'vue3-simple-typeahead';
import 'vue3-simple-typeahead/dist/vue3-simple-typeahead.css';
import NavHeader from './components/NavHeader.vue'
import StockForm from './components/StockForm.vue';
import ModelInformation from './components/ModelInformation.vue';
import StockDetail from './components/StockDetail.vue';
import ForecastedReturnsTable from './components/ForecastedReturnsTable.vue';
import ReturnsGraph from './components/ReturnsGraph.vue';

const app = createApp(App)

// Global registration
app.component('NavHeader', NavHeader);
app.component('StockForm', StockForm);
app.component('ModelInformation', ModelInformation);
app.component('StockDetail', StockDetail);
app.component('ForecastedReturnsTable', ForecastedReturnsTable);
app.component('ReturnsGraph', ReturnsGraph);
app.use(SimpleTypeahead);

const mountedApp = app.mount('#app')