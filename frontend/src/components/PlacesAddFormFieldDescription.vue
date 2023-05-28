<template>
    <form-group :validator="v">
      <textarea class="form__field" v-model="description" maxlength = "500" style="resize: none; height: 102px;" placeholder="Описание (до 500 символов)" @input="v.$touch()"></textarea>
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
        description: {
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
  