<template>
  <div>
    <div>
      <div class="d-flex justify-content-center">
        <SearchBar/>
      </div>
      <h1 style="margin-left: 30px;">🔥 오늘의 TOP 100 🔥</h1>
      <br>
    </div>
    <div v-if="getAllMoviesLength" class="row row-cols-2">
      <div v-for="movie in getAllMovies" :key="movie.id" class="col-2">
        <MovieCard :movie = "movie"/>
      </div>
    </div>
   
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'
import SearchBar from '@/components/SearchBar'

export default {
    name: 'AllMovieListView',
    components: {
      MovieCard,
      SearchBar,

    },
    computed: {
      getAllMovies() {
        return this.$store.state.all_movies
      },
      getAllMoviesLength() {
        return this.$store.state.all_movies?.length
      },

    }, 
    created(){
      console.log('created')
      this.$store.dispatch('loadMovies')
    }

}
</script>

<style>

.search_Bar{
  margin-top: 100px;
  width: 1000px;
  height: 50px;
}
.search-margin{
  margin-left: 800px;
  margin-bottom: 100px;
}


</style>