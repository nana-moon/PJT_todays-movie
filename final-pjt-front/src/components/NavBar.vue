<template>
  <div class="mb-4">
    <div class="navimg">
      <b-navbar type="dark pt-3" class="justify-content-between align-items-center">
        <b-navbar-nav class="logo">
          <b-nav-item v-if="!isLoggedIn">
            <router-link :to=" { name: 'login' }" class="text-decoration-none navfont">LOGIN</router-link>
          </b-nav-item>
          
          <!-- Navbar dropdowns -->
          <div v-if="isLoggedIn && currentUser.username" class="navdropdown">
            <b-nav-item-dropdown :text="currentUser.username" class="navfont" right>
                 
                <b-dropdown-item class="text-decoration-none text-black logoutbtn">
                  <router-link :to=" { name: 'profile', params: { username: currentUser.username } }"  class="text-decoration-none text-black" >
                    내 정보
                  </router-link>
                </b-dropdown-item>
              
              <b-dropdown-item @click="logout" class="text-decoration-none text-black logoutbtn">로그아웃</b-dropdown-item>
            </b-nav-item-dropdown>
          </div>

          <b-nav-item >
            <div @click.prevent="back" class="navfont" >GO BACK</div>
          </b-nav-item>

        </b-navbar-nav>

        <!-- 로고 -->
        <div>
          <h5 class="fw-bold logo"> 
              <router-link :to=" { name: 'home' }" class="text-decoration-none" style="font-size:40px">
                Today's Movie
              </router-link>        
          </h5>
        </div>

        <b-navbar-nav>
          <b-nav-item>
            <router-link :to=" { name: 'allMovies' }" class="text-decoration-none navfont">MOVIES</router-link>
          </b-nav-item>

          <b-nav-item v-if="isLoggedIn">
            <router-link :to=" { name: 'question' }" class="text-decoration-none navfont">TEST</router-link>
          </b-nav-item>

          <b-nav-item v-if="!isLoggedIn">
            <router-link :to=" { name: 'signup' }" class="text-decoration-none navfont">SIGN UP</router-link>
          </b-nav-item>
          
        </b-navbar-nav>
      </b-navbar>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'NavBar',
  
  methods: {
    ...mapActions(['logout', 'fetchSearchList']),
    back() {
    //   var referrer = document.referrer
    //   console.log(referrer)
    //   if (referrer.indexOf('/movies/save') !== -1) {
    //     return this.$router.push({ 
    //       name: 'recommendView', 
    //     })
    //   } else {
    //     return this.$router.go(-1)
    //   }
      return this.$router.go(-1)
    },
  },
  
  computed: {
    ...mapGetters(['isLoggedIn', 'currentUser']),
  },

}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Alfa+Slab+One&family=Fredoka+One&family=Permanent+Marker&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Hahmlet:wght@500&display=swap');

.search-margin{
  margin-left: 11rem;
  height: 3rem;
}
.mb-4{
  margin-right: 30px;
  margin-left: 30px;
}
.logo{
  font-family: 'Alfa Slab One', cursive;
font-family: 'Fredoka One', cursive;
font-family: 'Permanent Marker', cursive;
color: #42b983;
}

.logoutbtn{
  font-weight: bold;
  font-family: 'Hahmlet', serif;
}

router-link:hover{
  color: #42b983;
}

.navfont{
  font-size: x-large;
}
</style>