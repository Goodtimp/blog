<template>
  <div class="my-subhead">
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
  .my-subhead{
    padding:50px 0;
    color: black;
    text-align: center;
    background: transparent;
  }
  .my-subhead h1{
    font-family: "KaiTi","Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","\5FAE\8F6F\96C5\9ED1",Arial,sans-serif;
    font-size: 2.5em;
  }
  .my-subhead h1 small{
    color:#333;
    font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","\5FAE\8F6F\96C5\9ED1",Arial,sans-serif;
  }
</style>

