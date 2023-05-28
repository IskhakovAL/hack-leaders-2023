<template>
  <div style="position: relative; margin-top: 65px;">
    <BaseHeader />
    <!-- <BaseFormMultiselect /> -->
    {{this.getSearchPlatforms}}
    <SearchResultsFilters />
    <SearchResultsCards :cards="cards" />
  </div>
</template>
  
<script>
import BaseHeader from "@/components/BaseHeader.vue";
import SearchResultsFilters from "@/components/SearchResultsFilters.vue";
import SearchResultsCards from "@/components/SearchResultsCards.vue";
import {mapActions, mapGetters} from "vuex";
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
      cards: []
    }
  },
  created() {
    this.cards = this.getSearchPlatforms.map(item => ({
      id: item.platform_id,
      price: item.price,
      metro: {
        title: item.metro.title,
        color: item.metro.color
      },
    }))
  },
  methods: {
    ...mapActions(["fetchSearchPlatforms",])
  },
  async mounted() {
    await this.fetchSearchPlatforms();
  },
  computed: {
    ...mapGetters(["getSearchPlatforms"])
  }
};
</script>
  