<template>
    <div>
        <h1 class="registration__title">{{ title }}</h1>
        <registration-navbar-account style="margin-top: 16px"
            :link-tenant="navbarAccount.linkTenant"
            :link-landlord="navbarAccount.linkLandlord"
            :link-admin="navbarAccount.linkAdmin" />
        <registration-navbar-tenant v-if='tenantAccount'
            :link-natural-tenant="tenantAccount.linkNaturalTenant"
            :link-juridical-tenant="tenantAccount.linkJuridicalTenant" />
        <div style="margin-top: 16px">
            <registration-form-signin v-if="!form.isSignup" style="display: inline-block; vertical-align: top;" />
            <registration-form-signup-short v-else-if="!form.isLong" style="display: inline-block; vertical-align: top;" />
            <registration-form-signup-long is-landlord="is-landlord" v-else style="display: inline-block; vertical-align: top;"/>
            <router-link v-if="button" class="button button_size_m button_color_white" style="margin-left: 20px;" :to="button.link">{{ button.text }}</router-link>
        </div>
    </div>
</template>
  
<script>
import RegistrationNavbarAccount from "@/components/RegistrationNavbarAccount.vue";
import RegistrationNavbarTenant from "@/components/RegistrationNavbarTenant.vue";
import RegistrationFormSignin from "@/components/RegistrationFormSignin.vue";
import RegistrationFormSignupShort from "@/components/RegistrationFormSignupShort.vue";
import RegistrationFormSignupLong from "@/components/RegistrationFormSignupLong.vue";
export default {
    props: {
        title: String,
        navbarAccount: {
            linkTenant: String,
            linkLandlord: String,
            linkAdmin: String
        },
        tenantAccount: {
            linkNaturalTenant: String,
            linkJuridicalTenant: String
        },
        form: {
            isSignup: Boolean,
            isLong: Boolean
        },
        button: {
            link: String,
            text: String
        },
        isLandlord: Boolean
    },

    components: {
        RegistrationNavbarAccount,
        RegistrationNavbarTenant,
        RegistrationFormSignin,
        RegistrationFormSignupShort,
        RegistrationFormSignupLong
    },

}
</script>
    