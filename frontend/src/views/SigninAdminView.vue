<template>
  <div>
    <RegistrationPage class="registration"
      :title="title"
      :navbar-account="navbarAccount"
      :form="form"/>
  </div>
</template>

<script>
import RegistrationPage from "@/components/RegistrationPage.vue";
// import { mapActions, mapGetters } from "vuex";
export default {
  name: "SigninAdminView",

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
      }
    }
  },

  components: {
    RegistrationPage
  },

  // methods: {
  //   ...mapActions(["signin"]),
  //   ...mapGetters(["getIsLogin"]),
  //   async submitForm() {
  //     let data = new FormData();
  //     data.append("email", .);
  //     data.append("password", .);
  //     await this.signin(data);
  //   }
  // }
};
</script>
  