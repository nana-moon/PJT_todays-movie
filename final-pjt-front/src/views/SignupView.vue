<template>
  <div>
    <div v-if="!isLoggedIn" class="signup">
        <h2>SiGN UP</h2>
        <form @submit.prevent="signup(credentials)">
          <div>
              <input
                name="username"
                class="signUp--input__name"
                required
                autocomplete="username"
                placeholder="아이디를 적어주세요"
                onfocus="this.placeholder=''"
                onblur="this.placeholder='아이디를 적어주세요'"
                type="text"
                value=""
                v-model="credentials.username"
              />
          </div>
          <div>
              <input
                name="password"
                required
                class="signUp--input__pw"
                autocomplete="new-password"
                placeholder="비밀번호를 입력해주세요"
                onfocus="this.placeholder=''"
                onblur="this.placeholder=`비밀번호를 입력해주세요`"
                type="password"
                value=""
                v-model="credentials.password1"
  
              />
          </div>
          <div>
              <input
                name="confirmPassword"
                required
                class="signUp--input__pw"
                autocomplete="new-password"
                placeholder="비밀번호를 다시 한번 입력해주세요"
                onfocus="this.placeholder=''"
                onblur="this.placeholder='비밀번호를 다시 한번 입력해주세요'"
                type="password"
                value=""
                v-model="credentials.password2"
  
              />
          </div>
          <button type="submit" class="signupbtn"><span data-attr="회원">회원</span><span data-attr="가입">가입</span></button>
  
        </form>
    </div>

    <div v-if="isLoggedIn">
      <router-link :to=" { name: 'home' }" class="text-decoration-none" style="font-size:40px">
        메인으로 가기
      </router-link>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
name: 'SignupView',
data() {
  return {
    credentials: {
      username: '',
      password1:'',
      password2:'',
    }
  };
},
computed: {
  ...mapGetters(['isLoggedIn']),

},
methods: {
  ...mapActions(['signup']),
  signup(credentials) {
      if (credentials.password1 !== credentials.password2) {
        alert('비밀번호가 일치하지 않습니다.')
      } else {
        return this.$store.dispatch('signup', credentials)  
      }
    },
  },
};
</script>

<style>

.signupbtn{

margin-top:30px;
}
button {
  text-decoration: none;
  text-transform: uppercase;
  font-size: 30px;
  border: none;
  background-color: transparent;
  
}
button span {
  padding: 15px;
  transition: .5s;
  position: relative;
}
button span:nth-child(1) {
  color: #fff;
  background: #262626;
}
button span:nth-child(2) {
  color: #fff;
  background: #ff3636;
}
button span:nth-child(1):before {
  content: attr(data-attr);
  position: absolute;
  top: 0;
  left: 0;
  background: #ff3636;
  padding: 15px;
  transition: 0.5S;
  transform-origin: top;
  transform: rotateX(90deg) translateY(-50%);
}
button:hover span:nth-child(1):before {
  transform: rotateX(0deg) translateY(0%);
} 
button span:nth-child(2):before {
  content: attr(data-attr);
  position: absolute;
  top: 0;
  left: 0;
  background: #262626;
  padding: 15px;
  transition: 0.5S;
  transform-origin: bottom;
  transform: rotateX(90deg) translateY(50%);
}
button:hover span:nth-child(2):before {
  transform: rotateX(0deg) translateY(0%);
} 
button  span:nth-child(1):after {
content: attr(data-attr);
padding: 15px;
position: absolute;
top: 0;
left: 0;
background: #262626;
transform-origin: bottom;
transform: rotateX(0deg) translateY(0%);
transition: 0.5s;
}
button:hover span:nth-child(1):after {
transform: rotateX(90deg) translateY(50%);
}
button span:nth-child(2):after {
  content: attr(data-attr);
  position: absolute;
  top: 0;
  left: 0;
  background: #ff3636;
  padding: 15px;
  transition: 0.5S;
  transform-origin: top;
  transform: rotateX(0deg) translateY(0%);
}
button:hover span:nth-child(2):after {
  transform: rotateX(90deg) translateY(-50%);
} 
.signup{
top: 180px;
width: 500px;
height: 400px;
margin: 0px auto;
color: var(--font-color);
position: relative;
}
.signUp--input__id {
margin-bottom: 50px;
border-radius: 5px;
width: 500px;
height: 40px;
font-size: 15px;
color: black;
}
.signUp--input__name {
margin-bottom: 50px;
border-radius: 5px;
width: 500px;
height: 40px;
font-size: 15px;
color: black;
}
.signUp--input__pw {
margin-bottom: 15px;
border-radius: 5px;
width: 500px;
height: 40px;

font-size: 15px;
color: black;
}
</style>