<template>
  <div style="position: relative;">
    <BaseHeader />
    <l-map style="height: 1000px"
           class="mapStyle"
           :zoom="zoom"
           :center="center"
           :options="{attributionControl: false}">
      <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
      <l-marker :lat-lng="markerLatLng"></l-marker>
    </l-map>
  </div>
</template>


<script>
import BaseHeader from "@/components/BaseHeader.vue";
import { LMap, LTileLayer, LMarker } from 'vue2-leaflet';



export default {
  name: "SearchMapView",
  components: {
    BaseHeader,
    LMap,
    LTileLayer,
    LMarker
  },
  data () {
    return {
      url: 'https://{s}.tile.jawg.io/jawg-sunny/{z}/{x}/{y}{r}.png?access-token=vB4gFnPPNTu4qZCRPgEOOqu6sUyjyplvIBJ0WuHk66aSZcmc5K5BY8bz8vQgk19g',
      zoom: 15,
      center: [51.505, -0.159],
      markerLatLng: [51.504, -0.159]
    };

  },
};
</script>
<style>
.mapStyle {
  position: fixed;
  left: 50%;
  top: 65px;
  height: 1000px;
}

</style>