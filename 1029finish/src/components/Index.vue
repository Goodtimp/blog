
<template>
  <el-container class="el-carousel index-bg" style="height:100%">
    <v-aside></v-aside>
    <v-main>    </v-main>
  </el-container>
</template>
<script>
import aside from './share/ElAside'
import main from './ElMainIndex'
import cart from './indexcomponents/cart'
import Axios from 'axios'
import api from '../assets/api.js'

export default {
  name: "Index",
  data() {
    return {
      message: 1,
      carts: [],
    }
  },
  methods: {
  },
  mounted() {

  },
  components: {
    'v-cart': cart,
    'v-aside': aside,
    'v-main': main,
  }
}
</script>
<style>
body > .el-container {
  margin-bottom: 40px;
}
.index-bg{
  background-image: url("../../static/images/bg/bg-2.jpg");
  background-repeat: none;
  background-size: 100% 100%;
}

</style>

