<template>
  <el-main class="sub-main">
    <v-header :headline="categoryHeader.headline" :introduction="categoryHeader.introduction" :imgpath="categoryHeader.imgpath"></v-header>
    <v-cart-article style="margin:20px;" v-for="art in articles" :key="art.Id" :Likenum="art.Likenum" :id="art.Id" :hits="art.Hits" :cartImage="art.BackgroundPath" :title="art.ArticleName" :abstract="art.ArticleSuggests"></v-cart-article>
    <!--{{temp}}-->

  </el-main>
</template>
<script>
import cart from "./CartArticle"
import api from "../../assets/api.js"
import header from "./Header"

export default {
  data() {
    return {
      id: "",
      articles: [],
      //temp:[],
      categoryHeader: {
        id: "",
        bgImgPath: '',
        headline: '',
        introduction: '',
        imgpath: '',
      }
    }
  },
  methods: {
    GetSubId() {
      this.categoryHeader.id = this.$route.params.id;
    },
    GetHeaderMessage() {
      if (this.categoryHeader.id != 0) {
        api.getCategoryById(this.categoryHeader.id).then(data => {
          this.categoryHeader.bgImgPath = api.changeImagePath(data.BackgroundPath);
          this.categoryHeader.headline = data.CategoryName;
          this.categoryHeader.introduction = data.Intor;
          this.categoryHeader.imgpath = api.changeImagePath(data.CategoryLog);
        });
      }
      else{
          this.categoryHeader.headline = "ALL";
      }
    },//下面需要添加cart内容  根据cart内容实现点击跳转相应article页面
    GetArticle() {
      api.getSameArticleByCId(this.categoryHeader.id).then(data => {
        this.articles = data;
        //this.temp = data;
      })
    }
  },
  mounted() {
    this.GetSubId();
    this.GetHeaderMessage();
    this.GetArticle();
  },
  watch: {
    $route() {
      this.GetHeaderMessage();
    }
  },
  components: {
    "v-cart-article": cart,
    "v-header": header,

  },
  props: ['html']
}
</script>

<style>
.sub-main {
  color: black;
  text-align: center;
}
</style>
