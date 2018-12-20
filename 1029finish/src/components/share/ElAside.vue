
<template>
  <el-aside width="27%" id="left-aside">
    <v-toggle @child-msg="ToggleShow" :show="show"></v-toggle>
    <el-row style="margin-top:30%">
      <el-col :span="24">
        <div class="grid-content bg-purple-dark">
          <a><img src="../../../static/images/header.jpg" style="border-radius: 50%;" width="30%" /></a>
        </div>
      </el-col>
      <el-col style="margin-bottom:10px;" :span="18" :offset="3" v-for="cate in category" :key="cate.Id" :id="cate.Id">
        <a class="un" :href="'/subindex/'+cate.id">
          <div class="grid-content bg-purple-dark my-category">{{cate.CategoryName}}</div>
        </a>
      </el-col>
    </el-row>
    <v-footer></v-footer>
  </el-aside>
</template>

<script>
import api from '../../assets/api.js'
import toggle from './Toggle'
import common from '../../assets/common.js'
import footer from './Footer'
export default {
  data() {
    return {
       myWidth: (document.body.clientWidth),
      data: "",
      category: []
    }
  },
  methods: {
    Mobile() {
      var aside = $("#left-aside");
      if (common.IsMobile() && this.myWidth < 750) {
        var nowurl = window.location.href;
        if (!(nowurl.indexOf("subindex/0")>1 || nowurl.indexOf("article")>1)) {
          window.location.href = api.Root+"/subindex/0";
        }
        aside.hide();
        $(".my-ElAsideSign").hide();
      }
    },
    GetAllCategory() {
      api.getAllCategory().then(data => {
        for (var i = 0; i < data.length; i++) {
          this.category.push({ id: data[i].Id, CategoryName: data[i].CategoryName })
        }
        this.category.push({ id: 0, CategoryName: "All" })
      })
    },
    ToggleShow(val) {
      $("#left-aside").css('width', val ? '27%' : '0');
      $("#left-aside .my-ElAsideSign").css('position', val ? 'absolute' : 'relative')
    }
  },
  mounted() {
    this.GetAllCategory();
    this.ToggleShow(this.show);
        this.Mobile();
  },
  components: {
    'v-toggle': toggle,
    'v-footer':footer,
  },
  props: {
    show: {
      default: true
    }
  }
}
</script>

<style>
.el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  }
}
.my-category {
  border-radius: 15px;
}
.el-aside {
  background-color: rgba(12, 12, 12, 0.8);
  color: #fff;
  text-align: center;
  line-height: 4em;
}

.my-category:hover {
  background-color: rgb(145, 150, 150);
}
/* { "category": [ { "model": "blog.category", "pk": 1, "fields": { "CategoryName": "Python", "BackgroundPath": "/static/images/bg/bg-python.jpg", "CategoryLog": "/static/images/log/python-log.jpg", "Intor": "Simplicity is better than complexity.", "Id": 1 } }, { "model": "blog.category", "pk": 2, "fields": { "CategoryName": "ACM", "BackgroundPath": "/static/images/bg/bg-acm.jpg", "CategoryLog": "/static/images/log/acm-log.jpg", "Intor": "Anything can be solved by violence", "Id": 2 } }, { "model": "blog.category", "pk": 3, "fields": { "CategoryName": "Experience", "BackgroundPath": "/static/images/bg/bg-Experience.jpg", "CategoryLog": "/static/images/log/Experience-log.jpg", "Intor": "Some thoughts on the road", "Id": 3 } }, { "model": "blog.category", "pk": 4, "fields": { "CategoryName": "Others", "BackgroundPath": "null", "CategoryLog": "/static/images/log/others-log.jpg", "Intor": "Some other interesting code", "Id": 4 } }, { "model": "blog.category", "pk": 9, "fields": { "CategoryName": "test", "BackgroundPath": "images/category_back/53bf4fabe3f90.jpg", "CategoryLog": "images/category_log/596ec055e7d3b.jpg", "Intor": "Anything can be solved by violence", "Id": 9 } } ], "msg": "success", "error_num": 0 */
</style>


