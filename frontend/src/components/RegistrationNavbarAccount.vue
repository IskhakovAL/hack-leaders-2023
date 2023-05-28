<template>
    <div>
        <nav class="navbar">
            <router-link class="navbar__link" :to="linkTenant">Я ищу площадку</router-link>
            <router-link class="navbar__link" :to="linkLandlord">Я представляю площадки</router-link>
            <router-link class="navbar__link" :to="linkAdmin">Член АКИ</router-link>
        </nav>
        <router-view />
    </div>
</template>
    
<script>
export default {
    name: 'RegistrationNavbarAccount',

    props: {
        linkTenant: String,
        linkLandlord: String,
        linkAdmin: String
    }
};
</script>
  