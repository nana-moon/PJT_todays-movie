<template>
  <div class="signin">
    <h2>로그인</h2>
    <form @submit.prevent="login(credentials)">
    <div class="signin-input">
      <input
        type="text"
        class="signin-input__id"
        autocomplete="off"
        placeholder="아이디를 적어주세요"
        onfocus="this.placeholder=''"
        onblur="this.placeholder='아이디를 적어주세요'"
        required
        name="inputs"
        value=""
        v-model="credentials.username"

        />
    </div>
    <div class="signin-input">
      
      <input
        type="password"
        class="signin-input__pw"
        autocomplete="off"
        required
        placeholder="비밀번호를 입력해주세요"
        onfocus="this.placeholder=''"
        onblur="this.placeholder=`비밀번호를 입력해주세요`"
        v-model="credentials.password"
        />
      
    </div>
    <button class="learn-more login__button">LOGIN</button>
  </form>

</div>

</template>

<script>
import { mapActions } from 'vuex'

export default {
name:'LoginView',
data(){
  return{
    credentials:{
      username: '',
      password: '',
    }
  }
},
methods:{
  ...mapActions(['login'])
},

}


</script>

<style>
.signin{
top: 180px;
width: 500px;
height: 400px;
margin: 0px auto;
color: var(--font-color);
position: relative;
}

.signin-header {
font-size: 30px;
text-align: center;
height: 60px;
}
.signin-input__id,
.signin-input__pw {
  margin-bottom: 50px;
border-radius: 5px;
width: 500px;
height: 40px;
font-size: 15px;
color: black;
}

.signin-input__letter--id {
padding-left: 10px;
font-size: 15px;
position: absolute;
top: 105px;
width: 500px;
height: 40px;
}
.signin-input__letter--pw {
padding-left: 10px;
font-size: 15px;
position: absolute;
top: 180px;
width: 500px;
height: 40px;
}

.login__button {
margin-top: 40px;
margin-left: 50px;
font-size: 30px;
border: none;
width:400px;
}
</style>

<style lang="scss">
@import url('https://fonts.googleapis.com/css?family=Rubik:700&display=swap');

$bg: #fff;
$text: #382b22;
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
font-size: inherit;
font-family: inherit;
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