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
                <button class="button button_size_m button_color_pink" type="submit" :disabled="this.$v.$invalid">Создать аккаунт</button>
            </div>
        </form>
    </div>
</template>
  
<script>
import { required, email } from "vuelidate/lib/validators";
import { isTextCorrect, isPhoneEntered } from "@/validators";
import SignupFormFieldFirstName from "./SignupFormFieldFirstName.vue";
import SignupFormFieldSurname from "./SignupFormFieldSurname.vue";
import SignupFormFieldSecondName from "./SignupFormFieldSecondName.vue";
import BaseFormFieldEmail from "./BaseFormFieldEmail.vue";
import SignupFormFieldPhone from "./SignupFormFieldPhone.vue";

export default {
    name: "SignupFormShort",

    components: {
        SignupFormFieldFirstName,
        SignupFormFieldSurname,
        SignupFormFieldSecondName,
        BaseFormFieldEmail,
        SignupFormFieldPhone
    },

    data() {
        return {
            form: {
                firstName: "",
                surname: "",
                secondName: "",
                email: "",
                phone: ""
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
  