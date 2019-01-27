<template>
  <el-main style="text-align: center;">
    <v-header
      :ToolName="'英语演讲稿'"
      :introduction="'从指定网页利用爬虫，下载演讲稿以及翻译信息'"
    > </v-header>
    <div style="margin:100px 10% 50px 10%;text-indent:2em;">
      <a
        href="http://www.kekenet.com/Article/15539/"
        target="_blank"
      >网页链接</a>
    </div>
    <el-form :model="form">
      <el-form-item label="链接地址">
        <el-input
          type="textarea"
          v-model="form.url"
        ></el-input>
      </el-form-item>
    </el-form>

    <el-button
      style="margin:20px 0px;"
      v-on:click="getSpeech"
    >获取该篇</el-button>

    <div style="clear: both">
    </div>
<el-row :gutter="12">
  
  <el-col :offset="2" :span="20">
    <el-card shadow="hover">
      <div id="SpeechResult">

    </div>
    </el-card>
  </el-col>
  
</el-row>
    
  </el-main>
</template>
<script>
import exifheader from "./Header"
import upload from "../share/Upload"
export default {
  data() {
    return {
      data: [],
      imagepath: "",
      form: {
        url: ''
      }
    }
  },
  methods: {
    handleReslut(res) {
      if (res["return"] != 0) {
        if (this.common.IsMobile()) {//手机跳转页面
          window.location.href = this.api.Root + res['url'].substr(1);
        }
        else if ('download' in document.createElement('a')) {
          // 作为test.html文件下载
          this.api.funDownload(res["content"], res['name']);
        } else {
          eleButton.onclick = function () {
            this.$message({ message: '浏览器不支持', type: 'warning' });
          };
        }
      }
      else {
        this.$message({ message: "请求错误，请确认链接地址是否正确", type: 'warning' });
      }
    },
    getSpeech() {
      if (this.form.url == "") {
        this.$message({ message: '你还没添加链接呢！', type: 'warning' });
      }
      else {
        this.api.GetSpeech({ url: this.form.url }).then(res => {
          var key = 'huanhang';
          var content = res["content"].replace(new RegExp(key, 'g'), '<br/><br/>');
          $("#SpeechResult").html(content);
          this.$message({ message: "成功", type: 'success' });
         }).catch(res => {
          this.$message({ message: "输入格式不正确", type: 'Error' });
        })
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
#SpeechResult{
  text-align: left;
}
</style>

