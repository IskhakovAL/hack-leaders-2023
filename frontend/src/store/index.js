import Vue from 'vue'
import Vuex from 'vuex'
import user from './modules/user.js'
import platforms from "./modules/platforms";
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    user,
    platforms
  },
  plugins: [createPersistedState()]
})
