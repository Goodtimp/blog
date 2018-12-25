<template>

  <el-row class="cartRow">
    <el-col
      :span="10"
      :offset="2"
    >
      <div
        class="grid-content bg-purple"
        style="position: relative;"
      >
        <span class="badge"><i style="color:#fff;" :class="headermsg"></i></span>
        <h5 style="position: absolute;bottom: 5%;right: 2%;">
          <i
            class="el-icon-circle-check"
            style="color:#fff;"
          > {{Likenum}} &nbsp; </i>
          <i
            class="el-icon-view"
            style="color:#fff;"
          > {{Hits}}</i> </h5>
        <a :href="'/article/'+id"><img
            :src="cartImage"
            width="100%"
          /></a>
      </div>
    </el-col>
    <el-col
      :span="9"
      :offset="1"
      class="my-text"
    >
      <div class="grid-content bg-purple-light">
        <a :href="'/article/'+id">
          <h2>{{title}}</h2>
        </a>
        <p style="margin-top:10px;text-align:left; text-indent:2em;"> {{ abstract }}</p>
      </div>
    </el-col>
  </el-row>

</template>
<script>
import api from "../../assets/api.js"
import common from '../../assets/common.js'
export default {
  props: ['title','PostedTime', 'id', 'cartImage', 'abstract', 'Hits', 'Likenum'],
  data() {
    return {
      myWidth: (document.body.clientWidth),
      timer: false,
      headermsg:""
    }
  },
  methods: {
    getCartHeight() {
      $(".cartRow").find("img").on("load", function () {//图片加载后执行
        if (common.IsMobile()) {
          $("h2").css({ "font-size": "1em" });
          $("p").css({ "font-size": "0.75em" });
        }//修改手机端字体
        var father = $(this).parents(".cartRow");//获取父元素便于查找
        var height_intor = (parseInt($(this).height()) - parseInt(father.find("h2").height()) - 10);//获取引言的文字实际高度
        height_intor = height_intor - (height_intor % 23);//对最后一行进行处理，一行的固定高度为23px
        father.find("p").css({ "height": (height_intor + "px") });
      })
    },
    /**
     * 时时修改intor显示文字的多少
     */
    changeCartIntor() {
      $(".cartRow").find("img").each(function () {
        if (common.IsMobile()) {
          $("h2").css({ "font-size": "1em" });
          $("p").css({ "font-size": "0.75em" });
        }//修改手机端字体
        var father = $(this).parents(".cartRow");//获取父元素便于查找
        var height_intor = (parseInt($(this).height()) - parseInt(father.find("h2").height()) - 10);//获取引言的文字实际高度
        height_intor = height_intor - (height_intor % 23);//对最后一行进行处理，一行的固定高度为23px
        father.find("p").css({ "height": (height_intor + "px") });
      })
    },
    /**
     * 头部推荐文字
     */
    HeaderMassage(){
      if(this.Hits>300) this.headermsg="el-icon-star-off badgeshow";
      if((this.Hits>100&&this.Likenum>10)) this.headermsg="el-icon-star-on badgeshow";
      if(this.common.getDifferMonths(this.PostedTime)<1) this.headermsg="el-icon-news badgeshow";
    }
  },
  mounted() {
    window.onresize = () => {//窗口大小修改后
      return (() => {
        this.myWidth = document.body.clientWidth;
        this.changeCartIntor();
      })()
    },
    this.getCartHeight(),
    this.HeaderMassage()
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
.el-col {
  border-radius: 4px;
}
.cartRow {
  padding: 10px 0px;
  margin: 0px;
}
.my-text {
  color: #666;
  overflow: hidden;
}
h2 {
  color: black;
}
h2:hover {
  color: #666;
}
a,
a:link,
a:visited,
a:hover,
a:active {
  text-decoration: none;
  color: inherit;
}
.badge {
  position: absolute;
  display: inline-block;
  min-width: 10px;
  /* padding: 3px 7px; 修改为内部元素的margin，防止不需要显示时有多余背景*/
  font-size: 13px;
  font-weight: 700;
  line-height: 1;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  vertical-align: middle;
  background-color: #67c23a;
  border-radius: 10px;
}
.badgeshow{
  margin: 3px 7px;
}
</style>