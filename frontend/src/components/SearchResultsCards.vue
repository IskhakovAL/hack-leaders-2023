<template>
    <div>
        <ul class="search-results-cards list">
            <li v-for="card in cards" :key="card.id" class="search-results-cards__card">
                <img :src="card.image" :alt="card.title" class="search-results-cards__card-image"> 
                <h2 class="search-results-cards__card-title">{{ card.title }}</h2>
                <p class="search-results-cards__card-price">от {{ card.price }}₽/день</p>
                <p class="search-results-cards__card-metro">
                    <span :style="{ color: card.metro.color }">м</span>
                    {{ card.metro.title }}
                </p>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    name: "SearchResultCards",

    props: {
        cards: {
            type: Array,
            default: function(){
                return []
            }
        }
    }
}
</script>