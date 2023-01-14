import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import HomeView from './views/HomeView.vue'
import FriendView from './views/FriendView.vue'
import LoginView from './views/LoginView.vue'
import RegisterView from './views/RegisterView.vue'
import RankingView from './views/RankingView.vue'

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: () => import(/* webpackChunkName: "about" */ './views/AboutView.vue')
  },
  {
    path: '/play',
    name: 'game',
    component: () => import(/* webpackChunkName: "about" */ './views/GameView.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
