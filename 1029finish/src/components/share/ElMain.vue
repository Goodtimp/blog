<template>
  <el-main>
   {{html}}
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
body > .el-container {
  margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}
</style>
