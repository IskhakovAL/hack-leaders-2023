<template>
  <form-group :validator="v">
    <input class="form__field" type="tel" v-model="company" placeholder="Юрлицо" @input="v.$touch()">
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
    company: {
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
