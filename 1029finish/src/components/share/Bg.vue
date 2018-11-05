<template>
   <img :src="imgpath" class="back" id="Background">
</template>
<script>
export default {
  data(){
    return{
    }
  },
  props:['imgpath']
}
</script>

<style>
  .back{
position: fixed;
width: 100%;
height: 100%;

z-index: -100; 
}
</style>
