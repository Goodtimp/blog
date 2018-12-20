<template>
  <div class="my-header" :style="'position: relative;height:50%;background-image: url('+urlpath+');'" >
    <h1>{{title}}</h1>
    <br/>
    <h3>{{time}}</h3>
    <h4 style="position: absolute;
    bottom: 2%;
    right: 2%;"><i class="el-icon-view"></i> {{hits}}</h4>
  </div>
</template>
<script>
export default {
  data(){
    return{
      'height':"400",
    }
  },
  props:['title','time','urlpath','hits']
}
</script>
<style>
.my-header{
    color:white;
    padding-top:100px;
    text-align: center;
    margin-bottom:100px;
    background-size: 100% 100%;
    box-shadow: 0 2px 20px 0 rgba(0,0,0,.66);
}
.my-header h1{
  font-family:"楷体","KaiTi","Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
  font-size:3em;
}
.my-header h3,h4{
   font-family:"思源黑体",	"Source Han Sans CN","Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
}
</style>


