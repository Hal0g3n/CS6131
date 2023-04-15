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
        path: '/teams/:teamId',
        name: 'teams',
        component: () => import(/* webpackChunkName: "about" */ './views/TeamView.vue')
    },
    {
        path: '/teams',
        name: 'teams',
        component: () => import(/* webpackChunkName: "about" */ './views/TeamSearch.vue')
    },
    {
        path: '/tournament/:tourId',
        name: 'tournament',
        component: () => import(/* webpackChunkName: "about" */ './views/TournamentView.vue')
    },
    {
        path: '/tournament',
        name: 'tournament',
        component: () => import(/* webpackChunkName: "about" */ './views/TournamentSearch.vue')
    },
    {
        path: '/login',
        name: 'login',
        component: () => import(/* webpackChunkName: "about" */ './views/LoginView.vue')
    },
    {
        path: '/profile/:username',
        name: 'profile',
        component: () => import(/* webpackChunkName: "about" */ './views/UserProfile.vue')
    },
    {
        path: '/profile/',
        name: 'profile',
        component: () => import(/* webpackChunkName: "about" */ './views/UserSearch.vue')
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
