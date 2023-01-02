<template>
  <div class="search">
    <div class="d-flex align-items-center search-margin">     
      <b-form @submit.prevent="search">
        <b-form-input id="input-1" v-model="title" class="search_Bar" placeholder="🔎  영화를 검색하세요.">       
        </b-form-input>
      </b-form>
      <i class="fa-solid fa-magnifying-glass p-2"></i>
    </div>
  </div>
</template>

<script>
import { mapActions, } from 'vuex'

export default {
  name: 'SearchBar',
  data() {
    return {
      title: '',
    }
  },
    methods: {
      ...mapActions(['fetchSearchList',]),
      search() {
        this.$router.push({ name: 'movieSearchList', params:{ title: this.title } })
        this.fetchSearchList(this.title)
        this.title = ''
    },
  },
}
</script>

<style>
.search-margin{
  width: 1000px;
  margin-left: 150px;
}
</style>