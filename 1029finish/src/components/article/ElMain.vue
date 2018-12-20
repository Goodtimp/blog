<template>
   <el-main style="padding:0px;">
     <v-header :title="myheader.title" :time="myheader.postedtime" :hits="hits" :urlpath="myheader.urlpath"></v-header>
    
       <mavon-editor
      class="md my-content"
     :value="content"
     :subfield = "prop.subfield"
     :defaultOpen = "prop.defaultOpen"
     :toolbarsFlag = "prop.toolbarsFlag"
     :editable="prop.editable"
     :scrollStyle="prop.scrollStyle"
  ></mavon-editor>
     
      <v-footer :likenum="likenum" :islike="like"></v-footer>
 
   </el-main>
</template>
<script>
import head from "./Header"
import api from "../../assets/api.js"
import foot from "./Footer"
export default {
  data(){
    return{
      Comments:[],
      like: "",
      articleid: "",
      myheader: [],
      content:"",
      likenum:"",
      hits:"",
    }
  },
   methods: {
    GetArticleId() {
      let id = this.$route.params.id;
      this.articleid = id;
    },
    GetDetialMessage() {
      api.getArticleContentById(this.articleid).then(data => {
        this.like = data.like;
        this.hits=data.Hits;
        this.myheader.title = data.ArticleName;
        this.myheader.postedtime = data.PostedTime;
        this.myheader.urlpath = data.BackgroundPath;
        this.content = data.Content;
        this.likenum=data.Likenum;
        this.Comments=data.Comments;
      });
    }
  },
  computed: {
        prop () {
          let data = {
            subfield: false,// 单双栏模式
            defaultOpen: 'preview',//edit： 默认展示编辑区域 ， preview： 默认展示预览区域 
            editable: false,
            toolbarsFlag: false,
            scrollStyle: true
          }
          return data
        }
      },

  mounted() {
    this.GetArticleId();
    this.GetDetialMessage();
  },
  components:{
    "v-header":head,
    "v-footer":foot,
  },
}
</script>
<style>
.my-content{
  width:80%;
  margin:0 auto;
  margin-bottom: 100px;
}
</style>
