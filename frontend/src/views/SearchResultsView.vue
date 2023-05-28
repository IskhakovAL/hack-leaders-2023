<template>
  <div style="position: relative; margin-top: 65px;">
    <BaseHeader />
    <!-- <BaseFormMultiselect /> -->
    <SearchResultsFilters />
    <SearchResultsCards :cards="cards" />
  </div>
</template>
  
<script>
import BaseHeader from "@/components/BaseHeader.vue";
import SearchResultsFilters from "@/components/SearchResultsFilters.vue";
import SearchResultsCards from "@/components/SearchResultsCards.vue";
// import BaseFormMultiselect from "@/components/BaseFormFieldMultiselect.vue";
export default {
  name: "SearchResultsView",

  components: {
    BaseHeader,
    SearchResultsFilters,
    SearchResultsCards
    // BaseFormMultiselect
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
  