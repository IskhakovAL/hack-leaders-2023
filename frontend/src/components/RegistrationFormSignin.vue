<template>
    <div>
        <form class="form" @submit.prevent="submit" novalidate>
            <div class="form__column" style="width: 275px;">
                <base-form-field-email v-model="form.email" :v="$v.form.email" />
                <base-form-field-password v-model="form.password" :v="$v.form.password" />
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
import BaseFormFieldPassword from "@/components/BaseFormFieldPassword.vue";
import {mapActions, mapGetters} from "vuex";

export default {
    name: "SignupFormShort",

    components: {
      BaseFormFieldPassword,
        BaseFormFieldEmail
    },

    data() {
        return {
            form: {
                email: "",
                password: ""
            }
        };
    },

    validations: {
        form: {
            email: { required, email },
            password: { required }
        }
    },

    methods: {
      ...mapActions(["signIn", "fetchUser"]),
      ...mapGetters(["getIsLogin", "getUser"]),
      async submit() {
        console.log("submitted");
        this.$v.form.$touch();
        // if its still pending or an error is returned do not submit
        if (this.$v.form.$pending || this.$v.form.$error) return;
        // to form submit after this
        const data = new FormData();
        data.append("email", this.form.email);
        data.append("password", this.form.password);
        await this.signIn(data);
        await this.$router.push('/search/map')
        // if (this.getIsLogin) {
        //   await this.fetchUser();
        //   const userRole = this.getUser().role.title;
        //   if (userRole === "landlord") {
        //     await this.$router.push('/profile')
        //   } else if (userRole === "tenant") {
        //     await this.$router.push('/search/map')
        //   }
        // }
      }
    }
};
</script>
  