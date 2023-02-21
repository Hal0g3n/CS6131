import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import HomeView from './views/HomeView.vue'

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
        path: '/puzzles',
        name: 'puzzl',
        component: () => import(/* webpackChunkName: "about" */ './views/PuzzleView.vue')
    },
    {
        path: '/register',
        name: 'register',
        component: () => import(/* webpackChunkName: "about" */ './views/RegisterView.vue')
    },
    {
        path: '/friends',
        name: 'friends',
        component: () => import(/* webpackChunkName: "about" */ './views/FriendsView.vue')
    },
    {
        path: '/login',
        name: 'login',
        component: () => import(/* webpackChunkName: "about" */ './views/LoginView.vue')
    },
    {
        path: '/profile/:username',
        name: 'profile',
        component: () => import(/* webpackChunkName: "about" */ './views/ProfileView.vue')
    },
    {
        path: '/profile/',
        name: 'profile',
        component: () => import(/* webpackChunkName: "about" */ './views/ProfileView.vue')
    },
    {
        path: '/ranking',
        name: 'ranking',
        component: () => import(/* webpackChunkName: "about" */ './views/RankingView.vue')
    },
    {
        path: '/play',
        name: 'game',
        component: () => import(/* webpackChunkName: "about" */ './views/GameView.vue')
    },
    {
        path: '/feedback',
        name: 'feedback',
        component: () => import(/* webpackChunkName: "about" */ './views/FeedbackView.vue')
    },
    { path: "*", component: () => import(/* webpackChunkName: "about" */ './views/PageNotFound.vue') }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
