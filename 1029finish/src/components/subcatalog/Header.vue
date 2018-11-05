<template>
  <div class="my-head">
   <img :src="imgpath" width="36px"> &nbsp;
    <h1>
        {{ headline }} 
        
      <br/>
      <small>{{introduction}}</small></h1>
  </div>
</template>
<script>
export default {
  data(){
    return{
    }
  },
  props:['headline','introduction','imgpath']
}
</script>
<style>
  .my-head{
    padding:50px 0;
    color: black;
    text-align: center;
    background: transparent;
  }
  .my-head h1{
    font-size: 2.5em;
  }
</style>

