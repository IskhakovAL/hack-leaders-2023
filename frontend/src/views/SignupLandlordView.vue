<template>
  <div>
    <RegistrationPage class="registration"
      :title="title"
      :navbar-account="navbarAccount"
      :form="form"
      :button="button"
      :is-landlord="true"/>
  </div>
</template>

<script>
import RegistrationPage from "@/components/RegistrationPage.vue";
export default {
  name: "SignupLandlordView",

  data() {
    return {
      title: "Создайте аккаунт",
      navbarAccount: {
        linkTenant: "/signup/tenant-natural",
        linkLandlord: "/signup/landlord",
        linkAdmin: "/signin/admin"
      },
      form: {
        isSignup: true,
        isLong: true
      },
      button: {
        link: "/signin/landlord",
        text: "Войти в аккаунт"
      }
    }
  },

  components: {
    RegistrationPage
  },
};
</script>
  