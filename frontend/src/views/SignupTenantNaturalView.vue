<template>
  <div>
    <RegistrationPage class="registration" 
      :title="title"
      :navbar-account="navbarAccount"
      :tenant-account="tenantAccount"
      :form="form" 
      :button="button" />
  </div>
</template>

<script>
import RegistrationPage from "@/components/RegistrationPage.vue";
export default {
  name: "SignupTenantNaturalView",

  data() {
    return {
      title: "Создайте аккаунт",
      navbarAccount: {
        linkTenant: "/signup/tenant-natural",
        linkLandlord: "/signup/landlord",
        linkAdmin: "/signin/admin"
      },
      tenantAccount: {
        linkNaturalTenant: "/signup/tenant-natural",
        linkJuridicalTenant: "/signup/tenant-juridical"
      },
      form: {
        isSignup: true,
        isLong: false
      },
      button: {
        link: "/signin/tenant-natural",
        text: "Войти в аккаунт"
      }
    }
  },

  components: {
    RegistrationPage
  },
};
</script>
  