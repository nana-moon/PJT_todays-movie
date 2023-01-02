import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

import accounts from './modules/accounts'
import movies from './modules/movies'


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    all_movies:[],
  },
  getters: {
    all_movies: state => state.all_movies,

  },
  mutations: {
    LOAD_MOVIES(state, response) {
      console.log('mutations')
      console.log(response.data)
      state.all_movies = response.data
    },
  },
  actions: {
    // 초기 100개 영화 로드
    loadMovies(context) {
      const API_URL = 'http://localhost:8000'
      axios({
        method: 'get',
        url: `${API_URL}/movies/`,
      }).then((res) => {
        console.log(res)
        context.commit('LOAD_MOVIES', res)
      }).catch(err => console.log(err))

    }
  },
  // 모듈화
  modules: { accounts, movies,}
})