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
  name: "SigninTenantNaturalView",

  data() {
    return {
      title: "Войдите в аккаунт",
      navbarAccount: {
        linkTenant: "/signin/tenant-natural",
        linkLandlord: "/signin/landlord",
        linkAdmin: "/signin/admin"
      },
      tenantAccount: {
        linkNaturalTenant: "/signin/tenant-natural",
        linkJuridicalTenant: "/signin/tenant-juridical"
      },
      form: {
        isSignup: false
      },
      button: {
        link: "/signup/tenant-natural",
        text: "Создать аккаунт"
      }
    }
  },

  components: {
    RegistrationPage
  },
};
</script>
  