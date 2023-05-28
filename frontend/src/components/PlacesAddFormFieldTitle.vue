<template>
    <form-group :validator="v">
      <input class="form__field" type="text" v-model="title" placeholder="Название" @input="v.$touch()">
    </form-group>
  </template>
  
  <script>
  export default {
    props: {
      value: {
        type: String,
        default: ""
      },
  
      v: {
        type: Object,
        required: true
      }
    },
  
    computed: {
        title: {
        get() {
          return this.value;
        },
  
        set(value) {
          this.$emit("input", value);
        }
      }
    }
  };
  </script>
  