<template>
  <div style="position: relative;">
    <BaseHeader />
    <div style="width:100%; height: 100vh; background-color: gray;"></div>
  </div>
</template>
  
<script>
import BaseHeader from "@/components/BaseHeader.vue";
export default {
  name: "SearchMapView",
  components: {
    BaseHeader
  }
};
</script>
  