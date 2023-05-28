<template>
  <div>
    <h3>ProfileView</h3>
    <button @click="logout">Выйти из аккаунта</button>
  </div>
</template>
  
<script>
export default {
  name: "ProfileView",
  methods: {
    logout() {
      localStorage.clear();
      this.$router.push('/');
    }
  }
};
</script>
  