<template>
  <div :class="this.show?'my-toggle-left':'my-toggle-right'" @click="clickToggle">
    <i :class="this.show?'el-icon-arrow-left':'el-icon-arrow-right'"></i>
  </div>
</template>
<script>
export default {
  data() {
    return {
      show: true,
    }
  },
  methods: {
    clickToggle: function () {
      this.show = !this.show;
      this.$emit('child-msg', this.show)
    }
  },
  /*像父元素传递数据
  computed:{
    toggle:function(){
      return this.show
    }
  },*/
  props: {
    show: {
      default: true
    }
  }
}
</script>
<style>
.my-toggle-left {
  position: absolute;
  left: 25%;
  height: 100%;
  z-index: 100;
    cursor: pointer;
}

.my-toggle-right {
  cursor: pointer;
  position: absolute;
  left: 0.3%;
  height: 100%;
  z-index: 100;
}

i {
  position: relative;
  top: 45%;
  color: #999;
}
.my-toggle-right:hover i {
  color: white;
}
.my-toggle-left:hover i{
  color:white;
}
</style>

