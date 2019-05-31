<template>
  <el-container class="el-carousel" style="height:100%">
    <el-aside :show="0"></el-aside>
    <v-header></v-header>
    <el-main style="height:100%"></el-main>
  </el-container>
</template>
<script>
import aside from "../share/ElAside"
import main from "./ElMain"
import header from "../share/ElHeader"

export default {
  data() {
    return {
    }
  },
  components: {
    "el-main": main,
    "el-aside": aside,
    'v-header':header
  }
}
</script>
