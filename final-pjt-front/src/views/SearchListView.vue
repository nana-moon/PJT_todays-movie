<template>
  <div>
    <h1 v-if="searchMovieList.length">"{{ title }}"의 검색 결과 🎥</h1>
    <h1 v-if="!searchMovieList.length">"{{ title }}"의 검색 결과가 없습니다 😭</h1>

    <div>
      <div class="d-flex justify-content-center">
        <SearchBar/>
      </div>
    </div>

    <div v-if="searchMovieList" class="row row-cols-5">      
      <div v-for="movie in searchMovieList" :key="movie.id">
        <MovieCard :movie = "movie"/>
      </div>
    </div>
   
  </div>
  
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import MovieCard from '@/components/MovieCard'
import SearchBar from '@/components/SearchBar'

export default {
  name: 'SearchListView',
  components: {
    MovieCard,
    SearchBar,

  },
  computed:{
    ...mapGetters(['searchMovieList',]),
    title() {return this.$route.params.title}
  },
  methods:{
    ...mapActions(['fetchSearchList',]),
    
  },
  created(){
    this.fetchSearchList(this.$route.params.title)
  },

}
</script>

<style>
.search_Bar{
  width: 1000px;
  height: 50px;
}
.search-margin{
  margin-left: 800px;
  margin-bottom: 100px;
}

</style>