<template>
  <div class="comment_list">
    <comment-list-item
    v-for="comment in comments" :key="comment.id" :comment="comment">

    </comment-list-item>
  </div>
</template>

<script>
import CommentListItem from '@/components/CommentListItem'

export default {
  name:'CommentList',

  components:{
      CommentListItem,
  },
  props:{
      comments: Array,
  },
  methods:{
  }
}
</script>

<style>
.comment_list{
  margin: 30px;
}
</style>