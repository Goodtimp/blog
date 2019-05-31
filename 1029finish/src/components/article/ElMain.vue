<template>
  <el-main style="padding:0px;">

    <v-header
      :title="myheader.title"
      :time="myheader.postedtime"
      :hits="hits"
      :urlpath="myheader.urlpath"
    ></v-header>

    <mavon-editor
      style="line-height: 2em;"
      class="md my-content"
      :value="content"
      :ishljs="true"
      :subfield="prop.subfield"
      :defaultOpen="prop.defaultOpen"
      :toolbarsFlag="prop.toolbarsFlag"
      :editable="prop.editable"
      :scrollStyle="prop.scrollStyle"
    ></mavon-editor>

    <v-footer
      :likenum="likenum"
      :islike="like"
    ></v-footer>

  </el-main>
</template>
<script>
import head from "./Header"
import api from "../../assets/api.js"
import foot from "./Footer"
export default {
  data() {
    return {
      Comments: [],
      like: "",
      articleid: "",
      myheader: [],
      content: "",
      likenum: "",
      hits: "",
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
        this.hits = data.Hits;
        this.myheader.title = data.ArticleName;
        this.myheader.postedtime = data.PostedTime;
        this.myheader.urlpath = data.BackgroundPath;
        this.content = data.Content;
        this.likenum = data.Likenum;
        this.Comments = data.Comments;
      });
    }
  },
  computed: {
    prop() {
      let data = {
        bold: true, // 粗体
      italic: true, // 斜体
      header: true, // 标题
      underline: true, // 下划线
      strikethrough: true, // 中划线
      mark: true, // 标记
      superscript: true, // 上角标
      subscript: true, // 下角标
        subfield: false, // 单双栏模式
        defaultOpen: 'preview', //edit： 默认展示编辑区域 ， preview： 默认展示预览区域 
        editable: false,
        toolbarsFlag: false,
        scrollStyle: true,
         table: true, // 表格
          readmodel: true, // 沉浸式阅读
        // boxShadow:true //开启边框阴影
        ishljs: true,
      }
      return data
    }
  },

  mounted() {
    this.GetArticleId();
    this.GetDetialMessage();
  },
  components: {
    "v-header": head,
    "v-footer": foot,
  },
}
</script>
<style>
.my-content {
  width: 80%;
  margin: 0 auto;
  padding: 2px;
  
  margin-bottom: 100px;
  box-shadow: 0 2px 23px 0 rgba(0,0,0,.2);

   animation: myfirst 2s; 
    -moz-animation: myfirst 2s;     /* Firefox */
    -webkit-animation: myfirst 2s;  /* Safari 和 Chrome */
    -o-animation: myfirst 2s;       /* Opera */
}
.my-content pre{
border-radius: 2%!important
}
.my-content img{
  margin: 10px 0!important;
  max-height: 600px!important;
}
.hljs{
  background:#f6f8fa!important;
}
.my-content .v-show-content{
  background-color: white!important;
  padding-bottom: 2em;
}
.my-content a[target=_blank]{
  margin: 0 3px!important;
  border-bottom: 1px dotted #0366d6!important;
  word-break: break-all!important;
}
.my-content strong{
  margin:0 2px!important;
  color: #424242!important;
  font-weight:650!important;
}

.my-content a:hover{
  text-decoration:none!important;
  border-bottom: 1px solid #0366d6!important;
  color:#0074f8!important;
}
.my-content h1 h2{
  margin-top:2em!important;
  border-bottom: 2px solid #eaecef!important;
}
.my-content h3{
  margin-top:1.5em!important;
}
.markdown-body hr {
    height: .1em!important;
}
.my-content h1 h2 h3 h4 h5 h6{
    color: #424242!important;
}
@keyframes myfirst 
{
from {
    opacity: 0;
    bottom: -20px;
  }
  to {
    opacity: 1;
    bottom: 0px;
  }
}
@-webkit-keyframes myfirst {
  from {
    opacity: 0;
    bottom: -20px;
  }
  to {
    opacity: 1;
    bottom: 0px;
  }
}
pre .hljs{
  font-size: 1.3em;
}

@media screen and (max-width: 750px) {
  .my-content{
    width:100%;
    padding: 0px; 
    font-size: 90%!important;
  }
  .my-content .v-note-panel{
    box-shadow:none!important;
  }
  .my-content .v-show-content{
    padding: 6px!important;
  }
  
}
</style>
