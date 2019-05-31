<template>
  <div class="my-header" :style="'position: relative;background-image: url('+urlpath+');'" >
    <h1>{{title}}</h1>
    <br/><br/>
    <span>{{time}}</span>
    <h4><i class="el-icon-view"></i> {{hits}}</h4>
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
    height:40%;
    padding-top:100px;
    text-align: center;
    margin-bottom:100px;
    background-size: 100% 100%;
    box-shadow: 0px 4px 4px -1px rgba(0,0,0,.36);
}
.my-header h1{
  display: inline;
  background-color: rgba(1,1,1,0.15);
    padding: 0 0.5em;
    box-shadow: 0 2px 4px 0 rgba(0,0,0,.4);
  font-family:"楷体","KaiTi","Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
  font-size:3em;
  cursor: pointer;

   transition: background 0.3s;
  -moz-transition: background 0.3s; /* Firefox 4 */
  -webkit-transition: background 0.3s; /* Safari 和 Chrome */
  -o-transition: background 0.3s; /* Opera */
}
.my-header h1:hover{
  background-color: rgba(1,1,1,0.29);
}
.my-header span{
   margin-top:1em;
  background-color: rgba(1,1,1,0.15);
    padding: 0 1em;
    box-shadow: 0 2px 4px 0 rgba(0,0,0,.4);
   font-family:"思源黑体",	"Source Han Sans CN","Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
}
.my-header h4{
  position: absolute;
    bottom: 2%;
    right: 2%;
  background-color: rgba(1,1,1,0.15);
    padding: 0 0.5em;
    box-shadow: 0 2px 4px 0 rgba(0,0,0,.4);
   font-family:"思源黑体",	"Source Han Sans CN","Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
}
@media screen and (max-width: 750px) {
  .my-header{
    height:30%;
  }
  .my-header h1
  {
    font-size: 1.3em;
  }
  .my-header span{
    font-size: .9em;
  }
  .el-icon-view{
    font-size:.9em;
  }
}
</style>


