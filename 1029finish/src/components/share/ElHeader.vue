
<template>
  <el-header
    id="top-header"
    :class="this.show?'top-meau':'top-meau top-meau-off'"
    height="30px"
  >
  <i class="el-icon-s-unfold header-meau"
   @click="CloseHeader"></i>
    <el-row :gutter="20" style="margin-left:10px;" class="my-choise">
      <el-col
        :span="4"
        v-for="cate in category"
        :key="cate.Id"
        :id="cate.Id"
      ><a
          class="un"
          :href="'/subindex/'+cate.id"
        >
          <div class="grid-content bg-purple-dark my-category">
            <i :class="'header-sub-icon el-icon-blog-'+cate.CategoryName"></i>
           
          </div>
        </a>
      </el-col>

    </el-row>

  </el-header>
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
      show:""
    }
  },
  methods: {
    CloseHeader: function () {
      this.show=!this.show;
    },
    Mobile() {
      var header = $("#top-header");
      // console.log(document.body.clientWidth)
      if (document.body.clientWidth > 750) {
        // console.log(document.body.clientWidth)
         header.css("display","none");
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
  },
  mounted() {
    this.GetAllCategory()
    // 首先在Virtual DOM渲染数据时，设置下背景图的高度．
    this.Mobile()
    // 然后监听window的resize事件．在浏览器窗口变化时再设置下背景图高度．
  },
  components: {
  },

}
</script>

<style>
.top-meau {
  background-color: rgba(12, 12, 12, 0.8);
  color: white;
  text-align: center;
  line-height: 30px;
  position:absolute;
  width: 100%;
  z-index: 1501;

  transition: width 0.3s;
  -moz-transition: width 0.3s; /* Firefox 4 */
  -webkit-transition: width 0.3s; /* Safari 和 Chrome */
  -o-transition: width 0.3s; /* Opera */
}

.header-meau{
  position:absolute;
  z-index: 1501;
  left:10px;
  top:7px;
  cursor: pointer;
}
.my-choise{
  margin-left:10px;
}
.top-meau-off{
  width: 0;
}
.top-meau-off .my-choise{
  display: none;

}
.header-sub-icon{
  color:white;
}
</style>


