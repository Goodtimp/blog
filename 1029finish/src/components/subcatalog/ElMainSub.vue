<template>
  <el-main class="sub-main">
    <v-header
      :headline="categoryHeader.headline"
      :introduction="categoryHeader.introduction"
      :imgpath="categoryHeader.imgpath"
    ></v-header>
    <v-cart-article
      v-for="art in articles"
      :key="art.Id"
      :PostedTime="art.PostedTime"
      :Likenum="art.Likenum"
      :id="art.Id"
      :hits="art.Hits"
      :cartImage="art.BackgroundPath"
      :title="art.ArticleName"
      :abstract="art.ArticleSuggests"
    ></v-cart-article>
    <el-row>
      <el-button
        class="my-more-btn"
        size="big"
        @click="GetNextPage"
        :disabled="this.page<=0"
      >{{this.zhanyong===1?"加载中...":"加载更多"}}</el-button>
    </el-row>
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
      page: 1,
      zhanyong: 0,
      articles: [],
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
      if (this.categoryHeader.id > 0) {
        api.getCategoryById(this.categoryHeader.id).then(data => {
          this.categoryHeader.bgImgPath = api.changeImagePath(data.BackgroundPath);
          this.categoryHeader.headline = data.CategoryName;
          this.categoryHeader.introduction = data.Intor;
          this.categoryHeader.imgpath = api.changeImagePath(data.CategoryLog);
        });
      }
      else if (this.categoryHeader.id == -1) {
        this.categoryHeader.headline = "Hidden";
      }
      else {
        this.categoryHeader.headline = "ALL";
      }
    },//下面需要添加cart内容  根据cart内容实现点击跳转相应article页面
    GetArticle() {
      this.zhanyong = 1;
      api.getSameArticleByCId(this.categoryHeader.id).then(data => {
        this.articles = data;
        if (data.length != 5) this.page = 0;
        //this.temp = data;
          this.zhanyong = 0;
      })
    },
    GetNextPage() {
      if (this.page > 0 && this.zhanyong == 0) {
        this.zhanyong = 1;
        api.getSameArticleByCIdPage(this.categoryHeader.id, this.page).then(data => {
          this.articles = this.articles.concat(data);
          this.page++;
          if (data !== undefined && data.length != 5) this.page = 0;
             this.zhanyong = 0;
        })
      }
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
    },

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
.my-more-btn {
  margin: 70px 0 10px 0;
}
/* .more-btn:hover{
  background:white;
  color:rgba(12, 12, 12, 0.8);
} */
</style>
