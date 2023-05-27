<template>
  <div style="position: relative;">
    <BaseHeader />
    <BaseFormMultiselect />
    <SearchResultCards :cards="cards" />
  </div>
</template>
  
<script>
import BaseHeader from "@/components/BaseHeader.vue";
import SearchResultCards from "@/components/SearchResultCards.vue";
import BaseFormMultiselect from "@/components/BaseFormMultiselect.vue";
export default {
  name: "SearchResultsView",

  components: {
    BaseHeader,
    SearchResultCards,
    BaseFormMultiselect
  },

  data() {
    return {
      cards: [{
        id: 0,
        title: "Дом",
        image: require("../assets/card-template.jpg"),
        price: 20000,
        metro: {
          title: "Охотный ряд",
          color: "red"
        }
      },
      {
        id: 1,
        title: "Дом",
        image: require("../assets/card-template.jpg"),
        price: 20000,
        metro: {
          title: "Охотный ряд",
          color: "red"
        }
      },
      {
        id: 2,
        title: "Дом",
        image: require("../assets/card-template.jpg"),
        price: 20000,
        metro: {
          title: "Охотный ряд",
          color: "red"
        }
      },
      {
        id: 3,
        title: "Дом",
        image: require("../assets/card-template.jpg"),
        price: 20000,
        metro: {
          title: "Охотный ряд",
          color: "red"
        }
      },
      {
        id: 4,
        title: "Дом",
        image: require("../assets/card-template.jpg"),
        price: 20000,
        metro: {
          title: "Охотный ряд",
          color: "red"
        }
      },
      {
        id: 5,
        title: "Дом",
        image: require("../assets/card-template.jpg"),
        price: 20000,
        metro: {
          title: "Охотный ряд",
          color: "red"
        }
      },
      {
        id: 6,
        title: "Дом",
        image: require("../assets/card-template.jpg"),
        price: 20000,
        metro: {
          title: "Охотный ряд",
          color: "red"
        }
      }]
    }
  }
};
</script>
  