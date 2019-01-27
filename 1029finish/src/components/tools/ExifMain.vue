<template>
  <el-main style="text-align: center;">
    <v-header
      :ToolName="'EXif图片查看器'"
      :introduction="'上传原图，立即查看图像隐藏信息'"
    > </v-header>
    <div style="margin:100px 10% 50px 10%;text-indent:2em;">
      选择相机或者手机拍出的图片原图，你会看到图像隐藏了许多个人信息。包括你的拍摄时间、地点、使用的设备，甚至有没有开闪光灯...
      <br />当然我们测出的数据仅仅是英文版，这里给个链接可以翻译下。<a href="http://fanyi.baidu.com">点这里翻译</a>
      <br />上传图片过程可能长达十几秒，这取决于你的网速，请耐心等待，上传完成后会显示出上传图片点击查询便可查询信息。
    </div>
    <v-upload @child-msg="getpath"></v-upload>
    <el-button
      style="margin:20px 0px;"
      v-on:click="getExif"
    >查询</el-button>
    <div>
      <el-steps
        :active="1"
        v-for="(index, item) in data[0]" 
        :key="index"
        simple>
        <el-step
          :title="item"
          icon="el-icon-edit"
        ></el-step>
        <el-step :title="index"></el-step>
      </el-steps>

    </div>
  </el-main>
</template>
<script>
import Exif from 'exif-js'
import exifheader from "./Header"
import upload from "../share/Upload"
export default {
  data() {
    return {
      data: [],
      imagepath: ""
    }
  },
  methods: {
    getpath(val) {
      this.imagepath = val;
    },
    getExif() {
      var img = $("#uploadImage").get(0);
      if (img == null) {
        this.$message({ message: '你还没添加图片呢！', type: 'warning' });
      }
      else {
        var temp = this.data;
        Exif.getData(img, function () {
          temp.unshift(Exif.getAllTags(this));
          this.$message({ message: "成功", type: 'success' });
        });
      }
    }
  },
  components: {
    "v-header": exifheader,
    "v-upload": upload
  }
}
</script>
<style>
</style>

