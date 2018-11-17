/* jshint esversion: 6 */
import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
// import index from '@/components/index'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [{
    path: '/',
    name: 'Index',
    component: (resolve) => require(['@/components/index'], resolve)
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
  }
  ]
})
