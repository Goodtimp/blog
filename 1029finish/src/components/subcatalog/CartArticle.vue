<template>

  <el-row class="cartRow">
    <el-col :span="10" :offset="2">
      <div class="grid-content bg-purple">
        <a :href="'/article/'+id"><img :src="cartImage" width="100%" /></a>
      </div>
    </el-col>
    <el-col :span="9" :offset="1" class="my-text">
      <div class="grid-content bg-purple-light">
        <a :href="'/article/'+id">
          <h2>{{title}}</h2>
        </a>
        <p style="margin-top:10px;text-align:left; text-indent:2em;"> {{ abstract }}</p>
      </div>
    </el-col>

  </el-row>

</template>
<script>
import api from "../../assets/api.js"
export default {
  data() {
    return {
    }
  },
  methods: {
    getCartHeight() {
      $(".cartRow").find("img").each(function () {
        var father= $(this).parents(".cartRow");//获取父元素便于查找
        var height_intor=(Number($(this).height())-Number(father.find("h2").height())-10);//获取引言的文字实际高度
        height_intor=height_intor-(height_intor%23);//对最后一行进行处理，一行的固定高度为23px
     
        father.find("p").css({ "height": 
        (height_intor + "px")});
      })
    }
  },
  mounted(){
    this.getCartHeight();
  },
  props: ['title', 'id', 'cartImage', 'abstract']
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
.cartRow {
  padding: 10px 0px;
  margin: 0px;
}
.my-text {
  color: #666;
  overflow: hidden;
}
h2 {
  color: black;
}
h2:hover {
  color: #666;
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