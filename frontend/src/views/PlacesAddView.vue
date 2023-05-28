<template>
  <div>
    <BaseHeader />
    <PlacesAddForm style="margin: 80px 0 0 60px;" />
  </div>
</template>

<script>
import BaseHeader from "@/components/BaseHeader.vue";
import PlacesAddForm from "@/components/PlacesAddForm.vue";
export default {
  name: "PlacesAddView",

  components: {
    BaseHeader,
    PlacesAddForm
  }
};
</script>