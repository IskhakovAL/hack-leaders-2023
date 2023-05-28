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
  name: "SignupTenantJuridicalView",

  data() {
    return {
      title: "Создайте аккаунт",
      navbarAccount: {
        linkTenant: "/signup/tenant-juridical",
        linkLandlord: "/signup/landlord",
        linkAdmin: "/signin/admin"
      },
      tenantAccount: {
        linkNaturalTenant: "/signup/tenant-natural",
        linkJuridicalTenant: "/signup/tenant-juridical"
      },
      form: {
        isSignup: true,
        isLong: true
      },
      button: {
        link: "/signin/tenant-juridical",
        text: "Войти в аккаунт"
      }
    }
  },

  components: {
    RegistrationPage
  },
};
</script>
  