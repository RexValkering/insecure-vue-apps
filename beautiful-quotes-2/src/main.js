// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import 'bootstrap-css-only/css/bootstrap.min.css';
import 'mdbvue/build/css/mdb.css';
import Vue from 'vue';
import Vuex from 'vuex';
import VueRouter from 'vue-router';
import App from './App';
import { routes } from './routes';
import store from "@/store";

Vue.use(Vuex);
Vue.use(VueRouter);
Vue.config.productionTip = false;

const router = new VueRouter({
  routes,
  mode: 'history'
});

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
});
