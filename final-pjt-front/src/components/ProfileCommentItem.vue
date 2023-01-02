<template>
  <div>

    <router-link :to="{ name: 'MovieDetailView', params: { moviePk: comment.movie.id } }" class="router_link">
      <img :src="image_url" class="m-1 rounded-3 shadow-sm" style="height: 300px; width: 200px;"  alt="img">
        <p>{{ comment.movie.title }}</p>
    </router-link>
    <p class="fw-bold"> 리뷰: {{ comment.content }}</p>  

  </div>
</template>

<script>
export default {
  name: 'ProfileCommentItem',
  props: {
    comment: Object,
  },
  computed: {
      image_url(){
        console.log(this.comment.movie)
        return "https://image.tmdb.org/t/p/original"+ this.comment.movie.poster_path
      } 
    },
}

</script>

<style>

</style>
