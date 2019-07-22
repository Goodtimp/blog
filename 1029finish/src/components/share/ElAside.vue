
<template>
  <el-aside id="left-aside">
    <i
      class="el-icon-blog-guanbi my-guanbi"
      @click="CloseAside"
    ></i>
    <v-toggle
      @child-msg="ToggleShow"
      ref="mytoggle"
      :show="show"
    ></v-toggle>
    <el-row
      style="margin-top:30%"
      class="navigation"
    >
      <el-col :span="24">
        <div class="grid-content bg-purple-dark">
          <a><img
              src="../../../static/images/header.jpg"
              style="border-radius: 50%;"
              width="30%"
            /></a>
        </div>
      </el-col>
      <el-col
        class="my-subfont"
        :span="18"
        :offset="3"
        v-for="cate in category"
        :key="cate.Id"
        :id="cate.Id"
      >
        <a
          class="un"
          :href="'/subindex/'+cate.id"
        >
          <div class="grid-content bg-purple-dark my-category">
            <i :class="'sub-icon el-icon-blog-'+cate.CategoryName"></i>
            <span>{{cate.CategoryName}}</span>
          </div>
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
      data: "",
      category: [],
      screenWidth: document.body.clientWidth,
    }
  },
  methods: {
    CloseAside: function () {
      this.show = 0
      $(".my-guanbi").css("display", "none")
      this.$refs.mytoggle.hideenButton()
      this.ToggleShow(0)
    },
    Mobile() {
      var aside = $("#left-aside");
      if (this.screenWidth < 750) {
          aside.css("display","none");
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
      if (val === 0) {        $("#left-aside").css('width', '0');
        $(".my-guanbi").css("display", "none")      }
      else {
        $("#left-aside").css('width', val ? '21%' : '1.7em')
        $(".my-guanbi").css("display", "block")
      }
      // $(".el-aside .my-ElAsideSign").css('display', val ? '' : 'none')
      if (val) $("#left-aside").removeClass("el-aside-off")
      else $("#left-aside").addClass("el-aside-off")
    },
  },
  mounted() {
    this.GetAllCategory()
    this.ToggleShow(this.show)
    // 首先在Virtual DOM渲染数据时，设置下背景图的高度．
    this.Mobile()
    // 然后监听window的resize事件．在浏览器窗口变化时再设置下背景图高度．
    const that = this
    window.onresize = () => {
      return (() => {
        that.screenWidth = document.body.clientWidth
        if (that.screenWidth < 750) {
          if(this.show===true)
          {
            that.ToggleShow(false);
            this.$refs.mytoggle.hideenButton()
          }
        }
      })()
    }
  },
  components: {
    'v-toggle': toggle,
    'v-footer': footer,
  },
  props: {
    show: {
      default: document.body.clientWidth > 750
    }
  }
}
</script>

<style>
.my-guanbi {
  position: absolute;
  top: 10px;
  left: 7px;
  color:rgba(255, 255, 255, 0.2);
  font-size: 0.5em;
  cursor: pointer;
  transition: color 0.3s;
  -moz-transition: color 0.3s; /* Firefox 4 */
  -webkit-transition: color 0.3s; /* Safari 和 Chrome */
  -o-transition: color 0.3s; /* Opera */
}
.my-guanbi:hover{
  color:white;
}
.el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  }
}
.my-category {
  position: relative;
  border-radius: 15px;
  transition: background 0.3s;
  -moz-transition: background 0.3s; /* Firefox 4 */
  -webkit-transition: background 0.3s; /* Safari 和 Chrome */
  -o-transition: background 0.3s; /* Opera */
}
.el-aside {
  background-color: rgba(12, 12, 12, 0.8);
  color: #fff;
  
  text-align: center;
  line-height: 3.5em;
  transition: width 0.3s;
  -moz-transition: width 0.3s; /* Firefox 4 */
  -webkit-transition: width 0.3s; /* Safari 和 Chrome */
  -o-transition: width 0.3s; /* Opera */
}
.el-aside .my-subfont {
  margin-bottom: 10px;
}
.el-aside-off {
  background-color: rgba(12, 12, 12, 0.8);
  color: #fff;

  text-align: center;
  line-height: 4em;
  transition: width 0.3s;
  -moz-transition: width 0.3s; /* Firefox 4 */
  -webkit-transition: width 0.3s; /* Safari 和 Chrome */
  -o-transition: width 0.3s; /* Opera */
}
.el-aside-off .navigation {
  z-index: 120;
  padding-top: 40px;
}
.el-aside-off span,
.el-aside-off img {
  display: none;
}
.el-aside-off .my-ElAsideSign {
  display: none;
}

.el-aside-off .un i {
  display: initial;
  font-size: 1em;
}
.el-aside-off .my-subfont {
  margin-bottom: 3em;
}
.sub-icon {
  position: absolute;
  left: 3%;
  display: none;
  color: white;
}
.el-aside-off:hover {
}

.my-category:hover {
  background-color: rgb(145, 150, 150);
}
.my-category:hover > .sub-icon {
  display: block;
}

/* { "category": [ { "model": "blog.category", "pk": 1, "fields": { "CategoryName": "Python", "BackgroundPath": "/static/images/bg/bg-python.jpg", "CategoryLog": "/static/images/log/python-log.jpg", "Intor": "Simplicity is better than complexity.", "Id": 1 } }, { "model": "blog.category", "pk": 2, "fields": { "CategoryName": "ACM", "BackgroundPath": "/static/images/bg/bg-acm.jpg", "CategoryLog": "/static/images/log/acm-log.jpg", "Intor": "Anything can be solved by violence", "Id": 2 } }, { "model": "blog.category", "pk": 3, "fields": { "CategoryName": "Experience", "BackgroundPath": "/static/images/bg/bg-Experience.jpg", "CategoryLog": "/static/images/log/Experience-log.jpg", "Intor": "Some thoughts on the road", "Id": 3 } }, { "model": "blog.category", "pk": 4, "fields": { "CategoryName": "Others", "BackgroundPath": "null", "CategoryLog": "/static/images/log/others-log.jpg", "Intor": "Some other interesting code", "Id": 4 } }, { "model": "blog.category", "pk": 9, "fields": { "CategoryName": "test", "BackgroundPath": "images/category_back/53bf4fabe3f90.jpg", "CategoryLog": "images/category_log/596ec055e7d3b.jpg", "Intor": "Anything can be solved by violence", "Id": 9 } } ], "msg": "success", "error_num": 0 */

@media screen and (max-width: 750px) {

}
</style>


