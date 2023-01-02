<template>
  <div>
    <div v-if="!profileUser.username">
      <h2>사용자가 존재하지 않습니다.</h2>
    </div>

    <div>
      <div v-if="profileUser.username">
        <h2>{{profileUser.username}}님의 프로필 🏃‍♂️</h2>
      </div>

      <hr>

      <div v-if="!likeMovies">
        <p>담은 영화가 없습니다</p>
      </div>
      
      <div v-if="likeMovies">
        <h3>{{ profileUser.username }}님이 담아둔 영화</h3>
        
        <div class="row row-cols-2">
          <div v-for="movie in profileUser.like_movies" :key="movie.id" class="col-2">
            <movie-card :movie="movie" />
          </div>

        </div>
    
      </div>

      <hr>

      <div v-if="!commentCount">
        <p>영화 리뷰가 존재하지 않습니다.</p>
      </div>

      <div v-if="commentCount">
        <h3>{{ profileUser.username }}님의 영화 리뷰</h3>

        <div class="row row-cols-2">
          <div v-for="comment in profileUser.comments" :key="comment.id" class="col-2">
              <profile-comment-item :comment="comment"/>
          </div>
        </div>

      </div>

    
    </div>

    
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import MovieCard from '@/components/MovieCard'
import ProfileCommentItem from '@/components/ProfileCommentItem'

export default {
  name: 'ProfileView',
  components:{
    MovieCard,
    ProfileCommentItem,
  },
  computed:{
    ...mapGetters(['profileUser', 'currentUser']),
    getUsername(){
      return this.$route.params.username
    },
    commentCount(){
      return this.profileUser.comments?.length
    },
    likeMovies(){
      return this.profileUser.like_movies?.length
    },

  },
  methods:{
    ...mapActions(['fetchProfileUser',]),

  },
  created(){
    this.fetchProfileUser(this.getUsername)
  },
  watch: {
    $route(){
      this.fetchProfileUser(this.getUsername)
    }
  }
}
</script>

<style>

</style>