import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ProfileView from '../views/ProfileView.vue'
import SignupView from '@/views/SignupView'
import LoginView from '@/views/LoginView'
import AllMovieListView from '@/views/AllMovieListView'
import QuestionView from '@/components/QuestionView'

import SearchListView from '@/views/SearchListView'
import MovieDetailView from '@/components/MovieDetailView'
import RecommendView from '@/components/RecommendView'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },

  {
    path: '/movies/',
    name: 'allMovies',
    component: AllMovieListView
  },
  {
    path: '/accounts/login/',
    name: 'login',
    component:LoginView
  },
  {
    path: '/movies/search/:title/',
    name: 'movieSearchList',
    component: SearchListView
  },
  {
    path: '/movies/question/',
    name: 'question',
    component: QuestionView
  },
  {
    path:'/movies/save/',
    name:'recommendView',
    component: RecommendView

  },
  {
    path: '/movies/:moviePk/',
    name: 'MovieDetailView',
    component: MovieDetailView
  },
  
  {
    path:'/accounts/profile/:username/',
    name:'profile',
    component:ProfileView
  },

// save 원래 위치

  {
    path: '/accounts/signup/',
    name: 'signup',
    component:SignupView
  },



]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
