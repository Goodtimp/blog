<template>
  <div class="my-header" :style="'height:'+height+'px;background-image: url('+urlpath+');'" >
    <h1>{{title}}</h1>
    <br/>
    <h3>{{time}}</h3>
  </div>
</template>
<script>
export default {
  data(){
    return{
      'height':"300",
      'urlpath':"/static/images/bg/bg-1.jpg",
      'time':'2018-10-20 19:40'
    }
  },
  props:['title','time','urlpath']
}
</script>
<style>
  .my-header{
    color:white;
    padding-top:100px;
    text-align: center;
   
    background-size: 100% 100%;
}
.my-header h1{
  font-size:3em;
}
</style>


