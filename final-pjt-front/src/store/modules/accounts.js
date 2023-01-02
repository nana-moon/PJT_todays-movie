import drf from '@/api/drf'
import router from '@/router'
import axios from 'axios'

export default {
    state:{
      token: localStorage.getItem('token') || '',
      currentUser:{},
      authError: null,
      profileUser:{},
    },
    getters:{
      isLoggedIn: state => !!state.token,
      authHeader: state => ({ Authorization: `Token ${state.token}`}),
      // authError: state => state.authError,
      currentUser: state => state.currentUser,
      currentUsername: state=> state.currentUser.username,
      profileUser: state => state.profileUser
    },
    mutations:{
      SET_CURRENT_USER: (state, user) => state.currentUser = user,
      SET_TOKEN: (state, token) => state.token = token,
      // SET_AUTH_ERROR: (state, error) => state.authError = error,
      SET_PROFILE_USER: (state, user) => state.profileUser = user,
  
    },
    actions:{
      removeToken({ commit }){
        commit('SET_TOKEN', '')
        localStorage.setItem('token', '')
  
      },
      saveToken({ commit }, token){
        commit('SET_TOKEN', token)
        localStorage.setItem('token', token)
      },
      // 회원가입
      signup({ dispatch }, credentials){
        axios({
          method: 'POST',
          url: drf.accounts.signup(),
          data: credentials
        })
        .then(res=>{
          const token = res.data.key
          dispatch('saveToken', token)
          dispatch('fetchCurrentUser')
          router.push({ name: 'home'})
        })
        .catch(err=> {
          console.error(err.response.data)
          // commit('SET_AUTH_ERROR', err.response.data)
          alert('이미 존재하는 회원이거나 비밀번호가 너무 짧습니다.')
        })
  
      },
      // 로그인
      login({ dispatch }, credentials){
        axios({
          method: 'post',
          url: drf.accounts.login(),
          data: credentials
        })
        .then(res => {
          const token = res.data.key
          dispatch('saveToken', token)
          dispatch('fetchCurrentUser')
          // router.push({ name: 'home'})
          router.go(-1)
        })
        .catch(err => {
          console.error(err.response.data)
          // commit('SET_AUTH_ERROR', err.response.data)
          alert('입력 정보를 다시 확인해주세요.')
        })
      },
      // 로그아웃
      logout({getters, dispatch}){
        if (confirm('로그아웃 하시겠습니까?')) {
          axios({
            method: 'POST',
            url: drf.accounts.logout(),
            headers: getters.authHeader
          })
          .then(() => {
            dispatch('removeToken')
            dispatch('fetchCurrentUser')
            // location.reload()
          })
          .catch(err =>{
            console.error(err.response)
          })
        }
      },
  
      // 사용자 로그인상태 확인
      fetchCurrentUser({commit, getters, dispatch}){
        if (getters.isLoggedIn){
          axios({
            method: 'get',
            url: drf.accounts.currentUserInfo(),
            headers: getters.authHeader,
          })
          .then(res =>{
            commit('SET_CURRENT_USER', res.data)})
          .catch(err =>{
            if (err.response.status === 401 ) {
              dispatch('removeToken')
              router.push({ name: 'login' })
            }
          })
        }
      },
  
      // 프로필 유저 업데이트
      fetchProfileUser({commit}, username){
        axios({
          method: 'get',
          url: drf.accounts.profile(username),        
        })
        .then(res =>{

          console.log('프로필 유저 업데이트')
          console.log(res.data)
          
          commit('SET_PROFILE_USER', res.data)})
        .catch(err =>{
          console.error(err.response)
        })
      },
      follow({getters, dispatch}, username){      
        axios({
          method:'post',
          url: drf.accounts.follow(username),        
          headers: getters.authHeader,
        })
        .then(()=>{
          dispatch('fetchProfileUser', username)
        })
        .catch(err =>
          console.log(err.response))
      },
      
    },
    
  }