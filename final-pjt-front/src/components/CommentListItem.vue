<template>
  <div id="reload" class="comment-box">
    <div class="user-box d-flex">
       <div v-if="isLoggedIn">
            <button v-if="isLiked" @click="clickLike" >❤️</button>
            <button v-if="!isLiked" @click="clickLike">🤍</button>
          </div>

      <!-- 시작 -->
      <p class="ms-1 pt-0">
      
          <small>

            <router-link class="text-decoration-none" :to="{ name:'profile', params:{ username: comment.user.username} }">
          {{comment.user.username}}</router-link>
          </small>
      </p>
      
      <p class="text-muted text-end ms-2">
          <small> {{ comment.created_at | cutDate }}   </small>
      </p>
      <p v-if="likeCount"> &nbsp; 좋아요 {{ likeCount }}개</p>

      <span v-if="currentUser.username === comment.user.username && isLoggedIn" class="ms-2">
          <i class="text-muted text-end ms-2" @click="deleteComment(payload)">삭제</i>
      </span>
    </div>

    <p class="text-start" style="margin-left:40px;">
      {{ comment.content }}
    </p>

  </div>
</template>

<script>
import { mapActions, mapGetters} from 'vuex'

export default {
  name:'commentListItem',
  props:{
    comment: Object,
  },

  data(){
    return{
      payload: {
        moviePk: this.$route.params.moviePk,
        commentPk: this.comment.id,
      },
      isLiked: false,
    }
  },
  computed:{
    ...mapGetters(['currentUser', 'isLoggedIn', ]),
    likeCount(){
        return this.comment.like_users.length
    },
  },
  methods:{
    ...mapActions(['deleteComment', 'likeComment']),
    onLike() {
      const like_users = JSON.parse(JSON.stringify(this.comment.like_users))
      if (like_users.some(userPk => userPk === this.currentUser.pk)) {
        this.isLiked = true
      } else {
        this.isLiked = false
      }
    },
    clickLike() {
      this.likeComment(this.payload)
    }


  },
  filters:{
    cutDate(value){
      return value.slice(0, 10)
    }
  },
  
  created(){
    this.onLike()
  },
  updated() {
    this.onLike()
  }
}
</script>

<style>
</style>