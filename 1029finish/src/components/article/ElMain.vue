<template>
   <el-main style="padding:0px;">
     <v-header :title="myheader.title" :time="myheader.postedtime" :urlpath="myheader.urlpath"></v-header>
     <div v-html="content" class="my-content"></div>
    
   </el-main>
</template>
<script>
import head from "./Header"
import api from "../../assets/api.js"
export default {
  data(){
    return{
      ta: "",
      articleid: "",
      myheader: [],
      content: ""
    }
  },
   methods: {
    GetArticleId() {
      let id = this.$route.params.id;
      this.articleid = id;
    },
    GetDetialMessage() {
      api.getArticleContentById(this.articleid).then(data => {
        this.ta = data;
        this.myheader.title = data.ArticleName;
        this.myheader.postedtime = data.PostedTime;
        this.myheader.urlpath = data.BackgroundPath;
        this.content = data.Content;
      });
    }
  },
  mounted() {
    this.GetArticleId();
    this.GetDetialMessage();
  },
  components:{
    "v-header":head
  },
  props:['content']
}
</script>
<style>
.my-content{
  width:80%;
  margin:0 auto;
  margin-bottom: 100px;
}
</style>
