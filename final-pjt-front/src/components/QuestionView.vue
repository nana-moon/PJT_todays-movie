<template>
  <div class="all_question">
    <form @submit.prevent="submitQuestion(getResults)">

      <!-- 1 -->
      <div >
        <h2>오늘의 기분</h2>
        <b-form-group label="" v-slot="{ ariaDescribedby }">
          <b-form-radio-group
            id="btn-radios-1"
            v-model="firstSelected"
            :options="firstOptions"
            :aria-describedby="ariaDescribedby"
            name="radios-btn-default"
            buttons
          ></b-form-radio-group>
        </b-form-group>
        <div class="mt-3">오늘의 기분 : <strong>{{ firstSelected }}</strong></div>
      </div>
      <!-- 2 -->
      <br>
      <div>
        <h2>오늘의 날씨</h2>
        <b-form-group label="" v-slot="{ ariaDescribedby }">
          <b-form-radio-group
            id="btn-radios-1"
            v-model="secondSelected"
            :options="secondoptions"
            :aria-describedby="ariaDescribedby"
            name="radios-btn-default"
            buttons
          ></b-form-radio-group>
        </b-form-group>
        <div class="mt-3">오늘의 날씨 : <strong>{{ secondSelected }}</strong></div>
      </div>
      <!-- 3 -->
      <br>
      <div>
        <h2>오늘의 여유 시간</h2>
        <b-form-group label="" v-slot="{ ariaDescribedby }">
          <b-form-radio-group
            id="btn-radios-1"
            v-model="thirdSelected"
            :options="thirdOptions"
            :aria-describedby="ariaDescribedby"
            name="radios-btn-default"
            buttons
          ></b-form-radio-group>
        </b-form-group>
        <div class="mt-3">오늘의 여유 시간 : <strong>{{ thirdSelected }}</strong></div>
      </div>
      <!-- 4 -->
      <br>
      <div>
        <h2>오늘의 영화메이트</h2>    
        
        <b-form-group label="" v-slot="{ ariaDescribedby }">
          <b-form-radio-group
            id="btn-radios-1"
            v-model="fourthSelected"
            :options="fourthOptions"
            :aria-describedby="ariaDescribedby"
            name="radios-btn-default"
            buttons
          ></b-form-radio-group>
        </b-form-group>
        <div class="mt-3">오늘의 영화메이트 : <strong>{{ fourthSelected }}</strong></div>
      </div>
      <br>
      <button class="btn btn-primary btn-jittery">
        결과 확인❗❗❗
      </button>
    </form>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
    name : 'QuestionView',
    data() {
      return {
        firstSelected: '',
        firstOptions: [
          { text: '기분이 째져', value: 'good' },
          { text: '기분이 봉합됨', value: 'bad' },
        ],
        secondSelected: '',
        secondoptions: [
          { text: '맑음', value: 'sunny' },
          { text: '흐림', value: 'cloudy' },
          { text: '더움', value: 'hot' },
          { text: '추움', value: 'cold' },
        ],
        thirdSelected: '',
        thirdOptions: [
          { text: '1시간 30분 이내', value: 90 },
          { text: '2시간 이내', value: 120 },
          { text: '상관없음', value: 'free' },
        ],
        fourthSelected: '',
        fourthOptions: [
          { text: '혼자', value: 'alone' },
          { text: '커플', value: 'couple' },
          { text: '친구', value: 'friend' },
          { text: '가족', value: 'family' },
        ],

      }
    },
    computed: {
      ...mapGetters(['isLoggedIn']),
      getResults() {
        let results = {
          firstSelected: this.firstSelected,
          secondSelected: this.secondSelected,
          thirdSelected: this.thirdSelected,
          fourthSelected: this.fourthSelected,
        }
        return results
      },
    },

    methods: {
      submitQuestion(results) {
        if (results.firstSelected === "" || results.secondSelected === "" || results.thirdSelected === "" || results.fourthSelected === "") {
          alert('모든 문항을 선택해주세요.')
        } else if( !this.isLoggedIn ) {
          alert('로그인이 필요한 서비스입니다.')
          return this.$router.push({ name: 'login' })

        }else {
          return this.$store.dispatch('submitQuestion', results)         
        }
      }
    }


}
</script>

<style>
 h2 {
  font-family: 'Arial';
  text-transform: uppercase;
  font-weight: bold;
  font-size: 3rem;
  line-height: 0.75;
}
.all_question{
  top: 30px;
width: 500px;
height: 500px;
margin: 0px auto;
position: relative;
}

</style>


<style lang="scss">
.btn {
  margin: 1rem;
  &-jittery {
    animation: jittery 4s infinite;
  }

  &-icon {
    position: relative;
    margin-left: 8px;
    overflow: hidden;

    i {
      position: absolute;
      top: 41%;
      left: 48%;
      transform: scale(0.75) translate(-16%, 400%);
      transition: 0.2s;
    }

    span {
      display: flex;
      justify-content: center;
      align-items: center;
      transition: 0.2s;
    }

    &:hover {
      i {
        transform: scale(0.75) translate(-16%, 0);
      }

      span {
        transform: translateY(-400%);
      }
    }
  }

}


@keyframes jittery {
  5%,
  50% {
    transform: scale(1);
  }

  10% {
    transform: scale(0.9);
  }

  15% {
    transform: scale(1.15);
  }

  20% {
    transform: scale(1.15) rotate(-5deg);
  }

  25% {
    transform: scale(1.15) rotate(5deg);
  }

  30% {
    transform: scale(1.15) rotate(-3deg);
  }

  35% {
    transform: scale(1.15) rotate(2deg);
  }

  40% {
    transform: scale(1.15) rotate(0);
  }
}

@keyframes jelly {
  25% {
    transform: scale(0.9, 1.1);
  }

  50% {
    transform: scale(1.1, 0.9);
  }

  75% {
    transform: scale(0.95, 1.05);
  }
}

@keyframes pulse {
  from {
    box-shadow: 0 0 0 0 var(--btn-bg);
  }
}

@keyframes move-left {
  to {
    transform: translateX(-100%);
  }
}
</style>