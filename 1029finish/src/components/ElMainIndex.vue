<template>
  <el-main class="index-main">
      <h1 style="font-size:2em;margin-top:20%;">你好，我是这里的管家。<br/><br/><br/>
      <small>你可以点击左边导航栏，导航到你想要获取的内容分类。<br/>当然你也可以将左边导航栏隐藏。</small>
    </h1>
  </el-main>
</template>
<script>
export default {

  data() {

    return {}

  },
  props:['html']
}
</script>

<style>
 .index-main {
   position: relative;
    color: #fff;
    text-align: center;
  }
</style>
