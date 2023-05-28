<template>
    <div>
        <form class="form" @submit.prevent="submit" novalidate>
            <div class="form__column">
                <signup-form-field-first-name v-model="form.firstName" :v="$v.form.firstName" />
                <signup-form-field-surname v-model="form.surname" :v="$v.form.surname" />
                <signup-form-field-second-name v-model="form.secondName" :v="$v.form.secondName" />
                <base-form-field-email v-model="form.email" :v="$v.form.email" />
                <signup-form-field-phone v-model="form.phone" :v="$v.form.phone" />
            </div>
            <div class="form__column">
                <signup-form-field-position v-model="form.position" :v="$v.form.position" />
                <signup-form-field-company v-model="form.company" :v="$v.form.company" />
                <signup-form-field-inn v-model="form.inn" :v="$v.form.inn" />
                <base-form-field-password v-model="form.password" :v="$v.form.password" />
            </div>
            <div class="form__column">
                <button class="button button_size_m button_color_pink" type="submit" :disabled="this.$v.$invalid">Создать аккаунт</button>
            </div>
        </form>
    </div>
</template>
  
<script>
import { required, email } from "vuelidate/lib/validators";
import { isTextCorrect, isPhoneEntered, isInnNumeric, isInnLengthCorrect } from "@/validators";
import SignupFormFieldFirstName from "./SignupFormFieldFirstName.vue";
import SignupFormFieldSurname from "./SignupFormFieldSurname.vue";
import SignupFormFieldSecondName from "./SignupFormFieldSecondName.vue";
import BaseFormFieldEmail from "./BaseFormFieldEmail.vue";
import SignupFormFieldPhone from "./SignupFormFieldPhone.vue";
import SignupFormFieldPosition from "./SignupFormFieldPosition.vue";
import SignupFormFieldCompany from "./SignupFormFieldCompany.vue";
import SignupFormFieldInn from "./SignupFormFieldInn.vue";
import BaseFormFieldPassword from "@/components/BaseFormFieldPassword.vue";
import {mapActions, mapGetters} from "vuex";

export default {
    name: "SignupFormLong",

    props: {
      isLandlord: Boolean
    },

    components: {
      BaseFormFieldPassword,
        SignupFormFieldFirstName,
        SignupFormFieldSurname,
        SignupFormFieldSecondName,
        BaseFormFieldEmail,
        SignupFormFieldPhone,
        SignupFormFieldPosition,
        SignupFormFieldCompany,
        SignupFormFieldInn
    },

    data() {
        return {
            form: {
                firstName: "",
                surname: "",
                secondName: "",
                email: "",
                phone: "",
                position: "",
                company: "",
                inn: "",
                password: ""
            }
        };
    },

    validations: {
        form: {
            firstName: { required, isTextCorrect },
            surname: { required, isTextCorrect },
            secondName: { required, isTextCorrect },
            email: { required, email },
            phone: { required, isPhoneEntered },
            position: { required },
            company: { required },
            inn: { required, isInnNumeric, isInnLengthCorrect },
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
          data.append("repeat_password", this.form.password);
          data.append("juridical", true);
          data.append("landlord", this.isLandlord);
          data.append("first_name", this.form.firstName);
          data.append("second_name", this.form.secondName);
          data.append("phone", this.form.phone);
          data.append("surname", this.form.surname);
          data.append("position", this.form.position);
          data.append("title", this.form.company);
          data.append("inn", this.form.inn);
          await this.signUp(data);

        if (this.getIsLogin) {
          await this.fetchUser();
          const userRole = this.getUser().role.title;
          if (userRole === "landlord") {
            await this.$router.push('/profile')
          } else if (userRole === "tenant") {
            await this.$router.push('/search/map')
          }
        }
        }
    }
};
</script>
  