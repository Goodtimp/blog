// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
/* jshint esversion: 6 */
import 'element-ui/lib/theme-chalk/index.css';
import ElementUI from 'element-ui';
import Vue from 'vue';
import App from './App';
import router from './router';
import Axios from 'axios';
import $ from 'jquery';
import api from './assets/api.js';
import mavonEditor from 'mavon-editor';
import common from './assets/common.js';
import 'mavon-editor/dist/css/index.css';
// use
Vue.use(mavonEditor);
Vue.prototype.$axios = Axios;
Vue.prototype.api = api;// 定义全局
Vue.prototype.common = common;// 定义全局
Axios.defaults.headers.post['Content-Type'] = 'application/x-www-fromurlencodeed';
Vue.use(ElementUI, { size: 'small', zIndex: 3000 });
Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: {
    App
  },
  template: '<App/>',
  render: h => h(App)
});
