import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Vuelidate from "vuelidate";
import VuelidateErrorExtractor, { templates } from "vuelidate-error-extractor";
import "./assets/main.css";
import "./axios.js";

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
