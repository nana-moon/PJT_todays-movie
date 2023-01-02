<template>

  <div>
  <!-- <button v-if="isLiked" @click="clickLike">❤️</button>
  <button v-if="!isLiked" @click="clickLike">🤍</button> -->
    
  <router-link :to="{ name: 'MovieDetailView', params: { moviePk: movie.id } }" class="router_link">
    <img :src="image_url" class="m-1 rounded-3 shadow-sm" style="height: 300px; width: 200px;"  alt="img">
    <p>{{movie.title}}</p>
  </router-link>
  
  </div>

</template>

<script>
import { mapActions } from 'vuex'
export default {
    name:'MovieCard',
    props:{
      movie: Object,
    },
    computed: {
      image_url(){
        return "https://image.tmdb.org/t/p/original"+ this.movie.poster_path
      } 
    },
    methods: {
      ...mapActions(['fetchMovie'])
    }


}
</script>

<style>
.router_link{
  text-decoration: none;
  color: white;
}
.router_link :hover{
  color: white;
}
img :hover{
  color: white;
}
</style>