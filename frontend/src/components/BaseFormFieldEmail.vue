<template>
  <form-group :validator="v">
    <input class="form__field" type="email" v-model="email" placeholder="Электропочта" @input="v.$touch()">
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
    email: {
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
