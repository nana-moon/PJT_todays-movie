<template>
  <div>
    <h1>오늘의 추천 영화 👋</h1>
    <br>
    <div v-if="recommendedMovieList" class="row row-cols-2">
      <div v-for="movie in recommendedMovieList" :key="movie.id" class="col-2">
        <MovieCard :movie = "movie"/>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import MovieCard from '@/components/MovieCard'

export default {
  name: 'MovieSearchListView',
  data() {
    return {
        selectMovies: [],
    }
  },
  components: {
    MovieCard,

  },
  computed:{
    ...mapGetters(['recommendedMovieList',]),
  },
  methods:{
    
  },
  created(){

  },
}
</script>

<style>

</style>