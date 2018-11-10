
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
    <div class="my-sign">
      <i class="el-icon-message"> 879636706@qq.com</i><br/>
      <i class="el-icon-location"> 浙江·绍兴</i>
      <!--<i class="el-icon-success"></i>-->
    </div>
  </el-aside>
</template>

<script>
import api from '../../assets/api.js'
import toggle from './Toggle'
export default {
  data() {
    return {
      data: "",
      category: []
    }
  },
  methods: {
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
    $("#left-aside .my-sign").css('position',val?'absolute':'relative')
    }
  },
  mounted() {
    this.GetAllCategory();
    this.ToggleShow(this.show);
  },
  components: {
    'v-toggle': toggle
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
.my-sign{
  position: absolute;
  top:90%;
  left:7%;
  line-height: 2em;
  font-size:0.75em;
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
</style>
