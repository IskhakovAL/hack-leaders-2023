<template>
    <div>
        <nav class="navbar">
            <router-link class="navbar__link" :to="linkNaturalTenant">Я физлицо</router-link>
            <router-link class="navbar__link" :to="linkJuridicalTenant">Я юрлицо</router-link>
        </nav>
        <router-view />
    </div>
</template>
      
<script>
export default {
    name: 'RegistrationNavbarTenant',

    props: {
        linkNaturalTenant: String,
        linkJuridicalTenant: String
    }
};
</script>
  