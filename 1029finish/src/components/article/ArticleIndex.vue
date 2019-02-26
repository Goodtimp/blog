<template>
  <el-container class="el-carousel" style="height:100%">
    <el-aside :show="false"></el-aside>
    <el-main style="height:100%"></el-main>
   
  </el-container>
</template>
<script>
import aside from "../share/ElAside"
import main from "./ElMain"

export default {
  data() {
    return {
    }
  },
  components: {
    "el-main": main,
    "el-aside": aside,

  }
}
</script>
