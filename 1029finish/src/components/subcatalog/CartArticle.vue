<template>

  <el-row  class="cartRow">
    <el-col :span="10" :offset="2">
      <div class="grid-content bg-purple">
        <a :href="'/article/'+id"><img :src="cartImage" width="100%" /></a>
      </div>
    </el-col>
    <el-col :span="10" class="my-text">
      <div class="grid-content bg-purple-light">
        <a :href="'/article/'+id"><h3>{{title}}</h3></a>
        {{ abstract }}
      </div>
    </el-col>
   
  </el-row>

</template>
<script>
import api from "../../assets/api.js"
export default {
  data() {
    return {
      abstract:"First",
    }
  },
  props: ['title', 'id','cartImage']
}
</script>
<style>
.el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  }
}
.el-col {
  border-radius: 4px;
}
.cartRow{
 
  padding:10px 0px;
  margin:0px;
}
.my-text{
  color:#666;
}
h3{
  color:black;
}
h3:hover{
  color:#666;
}
a,
a:link,
a:visited,
a:hover,
a:active {
  text-decoration: none;
  color: inherit;
}
</style>