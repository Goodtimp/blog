<template>
<el-container class="el-carousel" style="height:100%">
       <v-aside></v-aside>
        <!-- <el-container> -->
             <v-header></v-header>
      <v-main>  </v-main>
    <!-- </el-container> -->
  </el-container>

  
</template>
<script>
import aside from "../share/ElAside"
import main from "./ElMainSub"
import header from "../share/ElHeader"

export default {
  data(){
    return{
      }
    },
  components:{
    "v-aside":aside,
    "v-main":main,
    'v-header':header
  }
}
</script>
<style>

</style>

