<template>
    <div>
        <form class="form" @submit.prevent="submit" novalidate>
            <div class="form__column">
                <base-form-field-email v-model="form.email" :v="$v.form.email" />
            </div>
            <div class="form__column">
                <button class="button button_size_m button_color_pink" type="submit" :disabled="this.$v.$invalid">Войти в аккаунт</button>
            </div>
        </form>
    </div>
</template>
  
<script>
import { required, email } from "vuelidate/lib/validators";
import BaseFormFieldEmail from "./BaseFormFieldEmail.vue";

export default {
    name: "SignupFormShort",

    components: {
        BaseFormFieldEmail
    },

    data() {
        return {
            form: {
                email: ""
            }
        };
    },

    validations: {
        form: {
            email: { required, email }
        }
    },

    methods: {
        submit() {
            console.log("submitted");
            this.$v.form.$touch();
            // if its still pending or an error is returned do not submit
            if (this.$v.form.$pending || this.$v.form.$error) return;
            // to form submit after this
            alert("Form submitted");
        }
    }
};
</script>
  