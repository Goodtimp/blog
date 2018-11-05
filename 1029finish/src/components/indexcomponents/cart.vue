<template>
  <div style="float:left;width:210px;height:310px;">
    <a :href="'/subindex/'+id">
   <el-button style="width:200px;height:300px;" round>
     <h1>{{ title }}</h1>
   </el-button>
   </a>
  </div>
</template>
<script>
export default {
  data(){
    return{
    }
  },
  props:['title','id']
}
</script>
<style>
.time {
    font-size: 13px;
    color: #999;
  }
  
  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  
  .clearfix:after {
      clear: both
  }
</style>

