<template>
  <div>
    <RegistrationPage class="registration"
      :title="title"
      :navbar-account="navbarAccount"
      :form="form"
      :button="button"/>
  </div>
</template>

<script>
import RegistrationPage from "@/components/RegistrationPage.vue";
export default {
  name: "SigninLandlordView",

  data() {
    return {
      title: "Войдите в аккаунт",
      navbarAccount: {
        linkTenant: "/signin/tenant-natural",
        linkLandlord: "/signin/landlord",
        linkAdmin: "/signin/admin"
      },
      form: {
        isSignup: false
      },
      button: {
        link: "/signup/landlord",
        text: "Создать аккаунт"
      }
    }
  },

  components: {
    RegistrationPage
  },
};
</script>
  