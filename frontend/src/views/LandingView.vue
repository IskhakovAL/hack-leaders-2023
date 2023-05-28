<template>
    <div style="background-color: #FAFAFA; display: flex;">
        <div class="landing">
            <section class="landing-header">
                <img class="landing-header__logo" src="../assets/logo.svg" alt="dorateam">
                <router-link class="button button_size_s button_color_pink" to="/signup/tenant-natural">Войти</router-link>
            </section>

            <section class="landing-main">
                <h1 class="landing-main__title">
                    Все креативные площадки Москвы в
                    <span class="landing-main__span">одном</span>
                    месте
                </h1>
                <p class="landing-main__description">
                    Смотрите сами
                </p>
            </section>

            <section class="landing-search">
                <h2 class="paragraph-title landing-search__title">Найдите площадку на&nbsp;свой вкус</h2>
                <p class="paragraph-text landing-search__text">Оптимальная система поиска и&nbsp;выдачи&nbsp;площадок на
                    карте</p>
                <img class="landing-search__image" src="../assets/landing-search.png" alt="Экраны поиска">
            </section>

            <section class="landing-add">
                <h2 class="paragraph-title landing-add__title">Разместите свою креативную площадку</h2>
                <p class="paragraph-text landing-add__text">Заполните карточку площадки, добавьте календарь и дело в шляпе!
                </p>
                <img class="landing-add__image" src="../assets/landing-add.png" alt="Экраны добавления">
            </section>

            <section class="landing-online">
                <h2 class="paragraph-title landing-online__title">Все преимущества онлайн-бронирования</h2>
                <p class="paragraph-text landing-online__text">Мгновенная бронь, автоматическое форматирование, электроннные
                    договоры и отзывы о площадках</p>
                <img class="landing-online__image" src="../assets/landing-online.png" alt="Экраны бронирования">
            </section>
        </div>

    </div>
</template>
  
<script>
export default {
    name: 'LandingView'
}
</script>

<style scoped>
.paragraph-title {
    margin: 0;
    padding: 0;
    width: 600px;
    font-weight: 700;
    font-size: 52px;
    line-height: 58px;
}

.paragraph-text {
    margin: 0;
    padding: 20px 0 0;
    width: 450px;
    font-weight: 400;
    font-size: 24px;
    line-height: 30px;
}

.landing {
    display: flex;
    flex-direction: column;
    background-color: #FAFAFA;
    position: relative;
    margin: 0 auto;
}

.landing-header {
    padding: 0 60px 0;
    box-sizing: border-box;
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    height: 65px;
    background-color: white;
    position: fixed;
    z-index: 3;
    top: 0;
    left: 0;
}

.landing-main {
    margin-top: 170px;
    width: 768px;
    display: flex;
    flex-direction: column;
    text-align: center;
    align-self: center;
}

.landing-main__title {
    margin: 0 0 0;
    padding: 0;
    font-weight: 700;
    font-size: 78px;
    line-height: 78px;
}

.landing-main__span {
    border-bottom: black 8px solid;
}

.landing-main__description {
    margin: 8px 0 0;
    padding: 0;
    font-weight: 400;
    font-size: 24px;
    line-height: 78px;
}

.landing-search {
    margin: 110px 0 0 60px;
    position: relative;
    height: 800px;
    max-width: 1280px;
}

.landing-search__title {
    margin-top: 30px;
}

.landing-search__image {
    width: 1430px;
    position: absolute;
    top: 114px;
    left: 130px;
}

.landing-add {
    height: 864px;
    position: relative;
}

.landing-add__title {
    padding-top: 140px;
    padding-left: 645px;
}

.landing-add__text {
    padding-left: 645px;
}

.landing-add__image {
    width: 1430px;
    position: absolute;
    top: 112px;
    left: -307px;
}

.landing-online {
    height: 619px;
    position: relative;
    margin-left: 60px;
}

.landing-online__title {
    padding-top: 112px;
}

.landing-online__image {
    width: 870px;
    position: absolute;
    top: 95px;
    left: 432px;
}
</style>