<template>
  <div class="multiselect-div">
    <Multiselect
      v-model="value"
      mode="tags" 
      :close-on-select="false" 
      :searchable="true"
      :options="field.options" 
      :placeholder="field.placeholder"
      class="multiselect-field" />
  </div>
</template>

<script>
import Multiselect from '@vueform/multiselect/dist/multiselect.vue2.js'

export default {
  components: {
    Multiselect,
  },

  props: {
    field: {
      placeholder: String,
      options: {
        // [{ value, label }, ...]
        type: Array,
        default: function(){
          return []
        }
      }
    }
  },

  data() {
    return {
      value: null,
    }
  }
}
</script>
  
<style scoped>
.multiselect-div {
  margin: 0;
  width: 144px;
  min-height: 24px;
  box-sizing: border-box;
}

.multiselect-field {
  min-height: 24px;
  width: 100%;
  --ms-font-size: 12px;
  --ms-line-height: 15px;
  --ms-border-color: #FF4261;
  --ms-border-color-active: #FF4261;
  --ms-radius: 6px;
  --ms-ring-color: #FFE8EC;
  --ms-placeholder-color: #CACACA;
  --ms-spinner-color: #FF4261;
  --ms-tag-font-size: 12px;
  --ms-tag-line-height: 15px;
  --ms-tag-font-weight: 500;
  --ms-tag-color: #FF4261;
  --ms-tag-bg: #FFE8EC;
  --ms-tag-bg-disabled: #CACACA;
  --ms-tag-radius: 6px;
  --ms-tag-remove-radius: 6px;
  --ms-option-font-size: 12px;
  --ms-option-line-height: 15px;
  --ms-option-color-pointed: black;
  --ms-option-bg-selected: #FF4261;
  --ms-option-color-disabled: #CACACA;
  --ms-option-bg-selected-pointed: #FF4261;
  --ms-option-color-selected-disabled: #FFE8EC;
  --ms-caret-color: #FF4261;
  --ms-clear-color: #FFE8EC;
  --ms-empty-color: #CACACA;
}
</style>
<style src="@vueform/multiselect/themes/default.css"></style>