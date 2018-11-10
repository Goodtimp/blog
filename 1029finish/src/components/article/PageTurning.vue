<template>
  <div style="width:80%;margin: 0 auto;padding-bottom:1px; margin-bottom: 50px;">
    <a :href="'/article/'+preart.Id"><i class="el-icon-d-arrow-left" style="float:left;"> {{preart.ArticleName}}</i></a>

    <a :href="'/article/'+nextart.Id"><i class="el-icon-" style="float:right;">{{nextart.ArticleName}} <i class="el-icon-d-arrow-right"></i></i></a>
  </div>
</template>
<script>
import api from "../../assets/api.js"
export default {
  data() {
    return {
      preart: [],
      nextart: [],
      articleid: ""
    }
  },
  methods: {
    GetArticleId() {
      let id = this.$route.params.id;
      this.articleid = id;
    },
    GetDetialMessage() {
      api.getArticleContentById(Number(this.articleid)-1).then(data => {
         if (data == null) {
          this.preart.ArticleName = "没有上一篇了";
          this.preart.Id = this.articleid;
        }
        else {
          this.preart = data;
        }
      });
      api.getArticleContentById(Number(this.articleid)+1).then(data => {
        if (data == null) {
          this.nextart.ArticleName = "没有下一篇了";
          this.nextart.Id = this.articleid;
          //this.nextart="12";
        }
        else {
          this.nextart = data;
        }
      });
    }
  },
  mounted() {
    this.GetArticleId();
    this.GetDetialMessage();
  },
}
</script>
