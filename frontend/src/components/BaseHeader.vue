<template>
    <div class="header">
        <img class="header__logo" src="../assets/logo.svg" alt="dorateam">
        <nav class="header__navbar">
            <router-link class="button button_size_s button_color_pink" to="/places/add">+ Разместить площадку</router-link>
            <router-link class="header__navbar-link" to="/search/map">Карта</router-link>
            <router-link class="header__navbar-link" to="/profile">Профиль</router-link>
        </nav>
    </div>
</template>
