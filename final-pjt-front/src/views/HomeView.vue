<template>
  <div class="home ">
    <div class="total"> 
    <div v-if="isLoggedIn" class="d-flex justify-content-center gap-5 homediv">
      <router-link :to="{ name: 'question' }" class="router_link">
        <button class="learn-more">
          오늘의 영화 추천 받기 👍👍
        </button>
      </router-link>
    </div>

    <div v-if="!isLoggedIn" class="d-flex justify-content-center gap-5 homediv">
      <router-link :to="{ name: 'login' }" class="router_link">
        <button class="learn-more">
          로그인 하고 오늘의 영화 추천 받기 👍👍
        </button>
      </router-link>
    </div>

    <div class="d-flex justify-content-center gap-5 homediv homediv2">
      <router-link :to="{ name: 'allMovies' }" class="router_link">
        <button class="learn-more">
          영화 리뷰 작성하기 GOGO 👉👉
        </button>
      </router-link>
    </div>
  </div>
</div>
</template>

<script>
// import { mapGetters, mapActions } from 'vuex'
import { mapGetters } from 'vuex'



export default {
  name: 'HomeView',
  components: {
  },
  computed: {
    ...mapGetters(['isLoggedIn', 'currentUser']),

  },
}
</script>

<style>

body {
  margin: 0;
  height: 100%;
  background-image: linear-gradient(to top, #d9afd9 0%, #97d9e1 100%);
  background-repeat: no-repeat;
  background-size: cover;
  background-attachment: fixed;
}
.home{
  top: 180px;
  margin: 0px auto;
  color: var(--font-color);
  position: relative;
}

.homediv2{
  margin: 250px;
  
}
.total{
  margin-left: 150px;
}

</style>


<style lang="scss">
@import url('https://fonts.googleapis.com/css?family=Rubik:700&display=swap');

$bg: #fff;
$text: black;
$light-pink: #fff0f0;
$pink: #ffe9e9;
$dark-pink: #f9c4d2;
$pink-border: #b18597;
$pink-shadow: #ffe3e2;

button {
margin-left: 135px;
position: relative;
display: inline-block;
cursor: pointer;
outline: none;
border: 0;
vertical-align: middle;
text-decoration: none;
&.learn-more {
  font-weight: 600;
  color: $text;
  text-transform: uppercase;
  padding: 1.25em 2em;
  background: $light-pink;
  border: 2px solid $pink-border;
  border-radius: 0.75em;
  transform-style: preserve-3d;
  transition: transform 150ms cubic-bezier(0, 0, 0.58, 1), background 150ms cubic-bezier(0, 0, 0.58, 1);
  &::before {
    position: absolute;
    content: '';
    width: 300px;
    height: 300px;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: $dark-pink;
    border-radius: inherit;
    box-shadow: 0 0 0 2px $pink-border, 0 0.625em 0 0 $pink-shadow;
    transform: translate3d(0, 0.75em, -1em);
    transition: transform 150ms cubic-bezier(0, 0, 0.58, 1), box-shadow 150ms cubic-bezier(0, 0, 0.58, 1);
  }
  &:hover {
    background: $pink;
    transform: translate(0, 0.25em);
    &::before {
      box-shadow: 0 0 0 2px $pink-border, 0 0.5em 0 0 $pink-shadow;
      transform: translate3d(0, 0.5em, -1em);
    }
  }
  &:active {
    background: $pink;
    transform: translate(0em, 0.75em);
    &::before {
      box-shadow: 0 0 0 2px $pink-border, 0 0 $pink-shadow;
      transform: translate3d(0, 0, -1em);
    }
  }
}
}

</style>