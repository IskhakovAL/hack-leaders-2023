import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Vuelidate from "vuelidate";
import VuelidateErrorExtractor, { templates } from "vuelidate-error-extractor";
import "./assets/main.css";
import "./axios.js";

import { Icon } from 'leaflet';
import { LMap, LTileLayer, LMarker } from 'vue2-leaflet';
import 'leaflet/dist/leaflet.css';

Vue.component('l-map', LMap);
Vue.component('l-tile-layer', LTileLayer);
Vue.component('l-marker', LMarker);





delete Icon.Default.prototype._getIconUrl;
Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
});

Vue.config.productionTip = false;

Vue.use(Vuelidate);
Vue.use(VuelidateErrorExtractor, {
  i18n: false,
  // Define common validation messages.
  messages: {
    required: "Обязательное поле.",
    isTextCorrect: "Поле '{attribute}' может содержать только буквы русского алфавита и знак '-'.",
    email: "Почта введена некорректно.",
    isPhoneEntered: "Обязательное поле.",
    isInnNumeric: "ИНН должен содержать только цифры.",
    isInnLengthCorrect: "ИНН должен содержать 10 или 12 символов."
  }
});

Vue.component("form-group", templates.singleErrorExtractor.foundation6);

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
