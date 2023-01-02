import drf from '@/api/drf'
import router from '@/router'
import axios from 'axios'

export default {
  state: {
    searchMovieList:{},
    movie: {},
    recommendedMovieList: {},
    movieimgUrl: null,
    moviebackimgUrl: null,

  },
  getters: {
    searchMovieList: state => state.searchMovieList,
    movie: state => state.movie,
    recommendedMovieList: state => state.recommendedMovieList,
    movieimgUrl: state => state.movieimgUrl,
    moviebackimgUrl: state => state.moviebackimgUrl,
  },
  mutations: {
    SET_SEARCH_MOVIES(state, movies) {
      state.searchMovieList = movies
    },
    SET_MOVIE(state, movie) {
      state.movie = movie
      state.movieimgUrl = 'https://image.tmdb.org/t/p/w500'+ movie.poster_path
      state.moviebackimgUrl = 'https://image.tmdb.org/t/p/w500'+ movie.backdrop_path
    },
    SET_RECOMMEND_MOVIE(state, movies) {
      state.recommendedMovieList = movies
    },

  },
  actions: {
    // 영화 검색 요청
    fetchSearchList({commit}, title){
      axios({
        method:'get',
        url: drf.movies.searchmovies(title),
      })
      .then(res=>{
        console.log('res')

        commit('SET_SEARCH_MOVIES', res.data)
      })
      .catch(err=>{
        console.log('err')
        console.error(err)
      })
    },
    // 영화 정보 업데이트
    fetchMovie({commit}, moviePk) {
      
      axios({
        methods: 'get',
        url: drf.movies.movie(moviePk),

      }).then(res => {
        console.log(res.data)
        commit('SET_MOVIE', res.data)

      }).catch(err=>{
        alert('데이터가 존재하지 않습니다.')
        console.error(err)
      })

    },
    // 코멘트 좋아요
    likeComment({getters, commit}, {moviePk, commentPk}) {
      axios({
        method: 'post',
        url: drf.movies.likecomment(moviePk, commentPk),
        headers: getters.authHeader,
      }).then((res)=>{
        // 다시 업데이트
        console.log(res.data)
        commit('SET_MOVIE', res.data)
      }).catch(err => 
        console.error(err))
    },
    // 영화 좋아요
    likeMovie({getters, dispatch}, moviePk) {
      axios({
        method: 'post',
        url: drf.movies.likemovie(moviePk),
        headers: getters.authHeader,
      }).then(()=>{
        // 다시 업데이트
        dispatch('fetchMovie', moviePk)
      }).catch(err => 
        console.error(err))
    },
    // 코멘트 달기
    createComment({getters, dispatch}, {moviePk, content}){
      const comment = { content }
      axios({
        method:'post',
        url: drf.movies.comments(moviePk),
        data: comment,
        headers: getters.authHeader,
      })
      .then(()=>{
        dispatch('fetchMovie', moviePk)
      })
      .catch(err =>
        console.log(err.response))
    },
    // 코멘트 삭제
    deleteComment({getters, dispatch}, {moviePk, commentPk}){
      if (confirm('댓글을 삭제하시겠습니까?')){
        axios({
          method: 'delete',
          url: drf.movies.comment(moviePk, commentPk),
          data: {},
          headers: getters.authHeader,
        })
        .then(() => {
          dispatch('fetchMovie', moviePk)
        })
        .catch(err =>
          console.log(err.response))
      }
    },
    // 설문 결과 바탕으로 영화 추천 요청
    submitQuestion({getters, commit}, results) {
      console.log(results)
      axios({
        method: 'post',
        url: drf.movies.question(),
        data: results,
        headers: getters.authHeader,
      })
      .then((res) => {
        console.log(res.data)
        commit('SET_RECOMMEND_MOVIE', res.data)

        router.push({ 
          name: 'recommendView', 
        })
      })
      .catch(err =>
        console.log(err.response))
    },

  }

}
