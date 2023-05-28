<template>
    <div class="multiselect-div" style="margin-top: 100px;">
      <Multiselect
      v-model="value"
      mode="tags"
      :close-on-select="false"
      :searchable="true"
      :create-option="true"
      :options="[
      { value: 'batman', label: 'Batman' },
      { value: 'robin', label: 'Robin' },
      { value: 'joker', label: 'Joker' },
    ]"
    class="multiselect-my"
  />
    </div>
  </template>
  
  <script>
    import Multiselect from '@vueform/multiselect/dist/multiselect.vue2.js'
  
    export default {
      components: {
        Multiselect,
      },
      data() {
        return {
          value: null,
          options: [
            'Batman',
            'Robin',
            'Joker',
          ]
        }
      }
    }
  </script>
  
  <style scoped>
  .multiselect-div {
    width: 275px;
    min-height: 32px;
    box-sizing: border-box;
    /* border: #FF4261 1px solid;
    border-radius: 6px;
    font-weight: 400;
    font-size: 16px;
    line-height: 20px; */
  }
  .multiselect-my {
    --ms-font-size: 16px;
    --ms-line-height: 20px;
    --ms-tag-bg: #DBEAFE;
    --ms-tag-color: #2563EB;
  }
  </style>
  <style src="@vueform/multiselect/themes/default.css"></style>