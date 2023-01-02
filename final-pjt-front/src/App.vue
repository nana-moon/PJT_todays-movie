<template>
  <div id="app">
    <nav>
      <nav-bar></nav-bar>
      <div class="padding">
        <router-view/>
      </div>
    </nav>
  </div>
</template>

<script>
// import axios from 'axios'
import NavBar from '@/components/NavBar.vue'

import { mapActions } from 'vuex'

export default {
  name: 'App',
  components:{
    NavBar
  },
  methods:{
    ...mapActions(['fetchCurrentUser'])
  },
  created(){
    this.fetchCurrentUser()
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Hahmlet:wght@500&display=swap');
#app {
  text-align: center;
  color: white;
  height: 100hv;
}
body {
  margin: 0;
  height: 100%;
  background-image: linear-gradient(to top, #d9afd9 0%, #97d9e1 100%);
  background-repeat: no-repeat;
  background-size: cover;
  background-attachment: fixed;
}

.padding {
  padding: 0vw 10vw;
  font-family: 'Hahmlet', serif;
}
nav {
  padding: 30px;
}
nav a {
  font-weight: bold;
  color:white;
}
nav a:hover{
  color: #42b983;
}

nav a.router-link-exact-active {
  color: #42b983;
}
nav router-link{
  color: white;
  font-family: 'Hahmlet', serif;
}

</style>