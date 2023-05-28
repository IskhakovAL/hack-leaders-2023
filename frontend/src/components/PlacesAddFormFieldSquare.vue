<template>
    <form-group :validator="v">
      <input class="form__field" type="number" v-model="square" min="0" max="100000" placeholder="Площадь" @input="v.$touch()">
    </form-group>
  </template>
  
  <script>
  export default {
    props: {
      value: {
        type: Number,
        default: 0
      },
  
      v: {
        type: Object,
        required: true
      }
    },
  
    computed: {
        square: {
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