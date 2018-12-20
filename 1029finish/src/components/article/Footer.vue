<template>
  <div class="my-like">
    <el-row>
      <el-button
        type="success"
        v-on:click="like"
        id="like"
        plain
      >点赞({{likenum}})</el-button>
    </el-row>
  <v-comments></v-comments>
    <div style="padding-top:100px;"></div>
  </div>
</template>
<script>
import api from "../../assets/api.js"
import comments from "./Comments"
export default {
  props: ['likenum'],
  data() {
    return {
      id: this.$route.params.id,
    }
  },
  methods: {
    like() {
      if (!$("#like").hasClass("my-sucesslike")) {
        api.AddLikeNum(this.id).then(res => {
          $("#like").addClass("my-sucesslike");
          $("#like").css("color", " #fff").css("background-color", "#67c23a").css("border-color", "#67c23a;");
          if (res.data.return == "1") {
            this.likenum = this.likenum + 1;
          }
        });
      }
    },
    startLike(){
      api.GetArticleLike(this.id).then(res=>{
        if(res.return=="0"){
          $("#like").addClass("my-sucesslike");
          $("#like").css("color", " #fff").css("background-color", "#67c23a").css("border-color", "#67c23a;");
        }
      });
    }
  },
 mounted(){
      this.startLike()
  },
   components:{
    "v-comments":comments,
  },
}
</script>
<style>
.my-like {
  width: 80%;
  margin: 0 auto;
  padding-bottom: 1px;
  margin-bottom: 50px;
  text-align: center;
}
#like {
  width: 100px;
  height: 50px;
  font-size: 1em;
}

.my-comment {
  margin-top: 20px;
  text-align: left;
}
.my-comment img {
  margin-right: 5px;
  width: 50px;
  height: 50px;
  vertical-align: middle;
  border-radius: 50%;
  -webkit-border-radius: 50%;
  -moz-border-radius: 50%;
}
.comment-body {
  margin-left: 10px;
  padding: 0px 0 10px 50px;
}
#addComment{
  border-color:#999;
  background-color:white
}
#addComment i{
    color: #999;
}

#addComment:hover i{ 
  color:black;
}
#addComment:hover {
  border-color: black;
}

</style>
