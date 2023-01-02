<template>
  <div>

    <h1 class="title" style="width:100%; color: #004159 ; text-shadow: 4px 2px 2px white;">{{ movie.title }}</h1>
    <div class="d-flex justify-content-between">
      <div>
        <img class="p-4" :src="movieimgUrl" style="height: 500px; width: 400px; " alt="영화 포스터"/>

        <!-- 좋아요 -->
        <div class="d-flex justify-content-between">
          <hr>

          <div v-if="!isLoggedIn">
            <p style="font-size:30px; width: 450px;" >❤️ {{ likeCount }}명의 찜</p>
          </div>

          <div v-if="isLoggedIn">
            <p v-if="isLiked" @click="clickLike" style="font-size:30px; width: 450px;" >❤️ {{ likeCount }}명의 찜</p>
            <p v-if="!isLiked" @click="clickLike" style="font-size:30px; width: 450px;">🤍 {{ likeCount }}명의 찜</p>
          </div>
        </div>
        
      </div>
      <p v-show="movie.tagline" class="text-start ps-2">"{{movie.tagline}}"</p>
      <hr>

      <div class="d-flex justify-content-start ps-2">
      </div>

      <div class="text-start ps-2">
        <span class="genres font_color" v-for="genre in movie.genres" :key="genre.id">{{genre.name}}</span>
        <p class="font_color"> 개봉일 : {{movie.release_date}} </p>
        <p> RunTime : {{movie.runtime}}분</p>
        <div class="fs-5 font_color">     
          <p class="pt-4 movie_overview">{{movie.overview}}</p>
        </div>
      </div>
      <hr>
    </div>


    <div class="comment-box" style="margin-left:20px;">
      <p class="text-start"><small>REVIEWS: {{ commentCount }}개</small>
      </p>
    </div>
      
      <comment-list :comments="movie.comments"></comment-list>

      <div v-if="isLoggedIn" >
        <comment-form></comment-form>
      </div>

      <p v-if="!isLoggedIn">
        <router-link :to="{ name:'login' }">댓글을 달려면 로그인</router-link>이 필요합니다.
      </p>
  
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

import CommentList from '@/components/CommentList'
import CommentForm from '@/components/CommentForm'

export default {
    name: 'MovieDetailView',
    components:{
      CommentForm, CommentList
    },
    data(){
      return{
        moviePk : this.$route.params.moviePk,
        isLiked: false,
      }
    },
    computed:{
      ...mapGetters(['movie', 'movieimgUrl', 'moviebackimgUrl', 'isLoggedIn','currentUser', ]),
      likeCount(){
        return this.movie.liked_count
      },
      commentCount() {
        return this.movie.comment_count
      }
    },

    methods:{
      ...mapActions(['fetchMovie', 'likeMovie']),
      onLike() {
        const like_users = JSON.parse(JSON.stringify(this.movie.like_users))
        // const like_users = this.movie.like_users
        console.log(like_users)
        if (like_users.some(user => user.pk === this.currentUser.pk)) {
          this.isLiked = true
        } else {
          this.isLiked = false
        }
      },
      clickLike() {
        const moviePk = this.movie.id
        this.likeMovie(moviePk)
      }
    },

    created() {
      this.fetchMovie(this.moviePk)
    },

    updated() {
      this.onLike()
    },
}
</script>

<style>
.genres:not(:first-of-type)::before{
  content: ", ";
}
.title{
  width: 400px;
  height: 100px;
  margin: 0px auto;
  color: var(--font-color);
  position: relative;
}
.font_color{
  color: #004159;
}


</style>