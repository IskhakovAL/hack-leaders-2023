<template>
  <div style="position: relative;">
    <BaseHeader />
    <l-map style="height: 1000px"
           class="mapStyle"
           :zoom="zoom"
           :center="center"
           :options="{attributionControl: false}">
      <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
      <l-marker
                :visible="markers.length !== 0"
                v-for="marker in markers"
                :key="marker.platformId"
                :lat-lng="[marker.latitude, marker.longitude]">

      </l-marker>
    </l-map>

    <search-results-filters style="margin-top: 65px"/>

    <search-results-cards style="margin-top: 65px" :cards="cards"/>

  </div>
</template>


<script>
import BaseHeader from "@/components/BaseHeader.vue";
import SearchResultsFilters from "@/components/SearchResultsFilters.vue";
import { LMap, LTileLayer, LMarker } from 'vue2-leaflet';
import SearchResultsCards from "@/components/SearchResultsCards.vue";
import {mapActions, mapGetters} from "vuex";



export default {
  name: "SearchMapView",
  components: {
    SearchResultsCards,
    BaseHeader,
    LMap,
    LTileLayer,
    LMarker,
    SearchResultsFilters
  },
  data () {
    return {
      url: 'https://{s}.tile.jawg.io/jawg-sunny/{z}/{x}/{y}{r}.png?access-token=vB4gFnPPNTu4qZCRPgEOOqu6sUyjyplvIBJ0WuHk66aSZcmc5K5BY8bz8vQgk19g',
      zoom: 12,
      center: [55.754398, 37.617880],
      markers: [],
      cards: []
    };

  },
  watch: {
    getSearchPlatforms(val) {
      this.cards = this.getSearchPlatforms.map(item => ({
        id: item.platform_id,
        title: item.title,
        image: 'http://178.170.197.108' + item.photos[0],
        price: item.price,
        metro: {
          title: item.metro[0].title,
          color: item.metro[0].color
        },
      }));
      this.markers = val.filter(item => {
        if (item.latitude !== null) {
          return {
            platformId: item.platform_id,
            latitude: parseFloat(item.latitude),
            longitude: parseFloat(item.longitude)
          }
        }
      });
    }
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
<style>
.mapStyle {
  position: fixed;
  left: 50%;
  top: 120px;
  height: 1000px;
}

</style>