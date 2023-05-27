<template>
  <form-group :validator="v">
    <input class="form__field" type="phone" v-model="phone" v-phonemask placeholder="Телефон" @input="v.$touch()">
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
    phone: {
      get() {
        return this.value;
      },

      set(value) {
        this.$emit("input", value);
      }
    }
  },

  directives: {
    phonemask: {
      bind(el) {
        el.oninput = function (e) {
          if (!e.isTrusted) {
            return;
          }
          const x = el.value.replace(/\D/g, '').match(/(\d{0,1})(\d{0,3})(\d{0,3})(\d{0,2})(\d{0,2})/);
          x[1] = '+7';
          el.value = !x[3] ? x[1] + ' (' + x[2] : x[1] + ' (' + x[2] + ') ' + x[3] + (x[4] ? '-' + x[4] : '') + (x[5] ? '-' + x[5] : '');
          el.dispatchEvent(new Event('input'));
        }
      },

      //   inserted: function (el) {
      //     el.mask()
      //   }
    }
  }
};
</script>
