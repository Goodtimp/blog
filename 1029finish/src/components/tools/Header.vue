<template>
  <div class="my-toolheader">
    <h1>
        {{ToolName}} 
      <br/>
      <small style="font-size:0.5em;">{{introduction}}</small></h1>
  </div>
</template>
<script>
export default {
  data(){
    return{
    }
  },
  props:['ToolName','introduction']
}
</script>
<style>
  .my-toolheader{
    text-align: center;
    height: 4em;
    margin-bottom: 2em;
  }
  .my-toolheader h1{
    font-family: "KaiTi","Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","\5FAE\8F6F\96C5\9ED1",Arial,sans-serif;
    font-size: 2em;
  }
  .my-toolheader h1 small{
   
    color:#333;
    font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","\5FAE\8F6F\96C5\9ED1",Arial,sans-serif;
  }
</style>

