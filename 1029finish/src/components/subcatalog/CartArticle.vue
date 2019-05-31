<template>

  <el-row class="cartRow">
    <el-col
      :span="11"
      :offset="1"
    >
      <div
        class="grid-content bg-purple father-img"
        style="position: relative;"
      >
        <span class="badge"><i
            style="color:#fff;"
            :class="headermsg"
          ></i></span>
           <a :href="'/article/'+id" class="cart-img-src">
        <div class="cartImageHover">
            <i class="el-icon-circle-check" style="color:#fff;"> {{Likenum}} &nbsp; </i>
          <i class="el-icon-view" style="color:#fff;"> {{Hits}}</i> 
          </div>
         
            <img class="cart-img"
            :src="cartImage"
            width="100%"/>
          </a>
          
        <h5 class="num-like-hits">
          <i
            class="el-icon-circle-check"
            style="color:#fff;"
          > {{Likenum}} &nbsp; </i>
          <i
            class="el-icon-view"
            style="color:#fff;"
          > {{Hits}}</i> </h5>
        
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
  props: ['title', 'PostedTime', 'id', 'cartImage', 'abstract', 'Hits', 'Likenum'],
  data() {
    return {
      myWidth: (document.body.clientWidth),
      timer: false,
      headermsg: ""
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
    HeaderMassage() {
      if (this.Hits > 300) this.headermsg = "el-icon-star-off badgeshow";
      if ((this.Hits > 100 && this.Likenum > 10)) this.headermsg = "el-icon-star-on badgeshow";
      if (this.common.getDifferMonths(this.PostedTime) < 1) this.headermsg = "el-icon-news badgeshow";
    }
  },
  mounted() {
    const that = this;
    window.addEventListener('resize', function () { //防止resize 覆盖
      that.myWidth = document.body.clientWidth;
      that.changeCartIntor();
    })
    // window.onresize = () => {//窗口大小修改后
    //   return (() => {
    //     this.myWidth = document.body.clientWidth;
    //     this.changeCartIntor();
    //   })()
    // },
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
  /* opacity:0; */
  padding: 10px 0px;
  margin: 0px;
  animation: cartmove .8s 1;
  /* animation-play-state:paused; */
  -webkit-animation: cartmove .8s 1; /* Safari 和 Chrome */
}
.cartRowMove {
  animation-play-state: running;
}
@keyframes cartmove {
  from {
    opacity: 0;
    bottom: -20px;
  }
  to {
    opacity: 1;
    bottom: 0px;
  }
}
@-webkit-keyframes cartmove {
  from {
    opacity: 0;
    bottom: -20px;
  }
  to {
    opacity: 1;
    bottom: 0px;
  }
}
.grid-content h2{
  padding-bottom: 5px;
  border-bottom: 2px solid #eaecef!important;
}

.cartImageHover{
    position: absolute;
    height: 100%;
    width: 100%;
    z-index:-1;
     transition: background 0.3s;
  -moz-transition: background 0.3s; /* Firefox 4 */
  -webkit-transition: background 0.3s; /* Safari 和 Chrome */
  -o-transition: background 0.3s; /* Opera */
}
.num-like-hits{
  position: absolute;bottom: 5%;right: 2%;
  background-color: rgba(100,100,105,0.2);
   padding: 1px 3px;
   box-shadow: 0 1px 3px 0 rgba(0,0,0,.66);
}
.cart-img,.cartImageHover,.father-img{
   border-radius:3%;
   cursor: pointer;
}
.father-img:hover .cartImageHover{
  z-index:1;
  background-color: rgba(50, 50, 50, 0.4);
}
.father-img:hover h5{
  display:none;
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
.badgeshow {
  margin: 3px 7px;
}
@media screen and (max-width:750) {
  .cartRow{
    margin: 0px!important;
  }
  .grid-content h2{
  border: 0;
}
}
</style>