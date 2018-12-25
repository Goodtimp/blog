/* jshint esversion: 6 */
import Vue from 'vue';
import Router from 'vue-router';
// import HelloWorld from '@/components/HelloWorld'
// import index from '@/components/index'

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [{
    path: '/tools/Exif',
    name: 'Exif',
    component: e => require(['@/components/tools/Exif.vue'], e)
  },
  {
    path: '/tools/speech',
    name: 'Speech',
    component: e => require(['@/components/tools/Speech.vue'], e)
  },
  {
    path: '/subindex/:id',
    name: 'subindex',
    component: e => require(['@/components/subcatalog/SubIndex.vue'], e)
  },
  {
    path: '/article/:id',
    name: 'article',
    component: e => require(['@/components/article/ArticleIndex.vue'], e)
  },
  {
    path: '/',
    name: 'Index',
    component: (resolve) => require(['@/components/index'], resolve)
  }
  ]
});
