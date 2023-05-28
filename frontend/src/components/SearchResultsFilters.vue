<template>
    <div style="display: flex">
        <BaseFormFieldMultiselect :field="fieldIndustry" />
        <BaseFormFieldMultiselect :field="fieldMetro" />
        <BaseFormFieldMultiselect :field="fieldEquipments" />
        <BaseFormFieldMultiselect :field="fieldAccessabilities" />
        <BaseFormFieldMultiselect :field="fieldFacilities" />
        <router-link class="button" :to="linkJuridicalTenant">Я юрлицо</router-link>
        <filter-form-field-from-to title="Стоимость"/>
        <filter-form-field-from-to title="Площадь"/>
        <filter-form-field-from-to title="Количество человек"/>
    </div>
</template>

<script>
import BaseFormFieldMultiselect from './BaseFormFieldMultiselect.vue';
import FilterFormFieldFromTo from './FilterFormFieldFromTo.vue';
import {mapActions, mapGetters} from "vuex";
export default {
    name: "SearchResultsCards",

    data() {
        return {
            fieldIndustry: { // Индустрии
                placeholder: "Индустрия",
                options: []
            },
            fieldMetro: { // Станции метро
                placeholder: "Метро",
                options: [ ]
            },
            fieldEquipments: { // Оборудование
                placeholder: "Оборудование",
                options: []
            },
            fieldAccessabilities: { // Доступность
                placeholder: "Доступность",
                options: []
            },
            fieldFacilities: { // Удобства
                placeholder: "Удобства",
                options: []
            }
        }
    },
    created() {
      this.fieldIndustry.options = this.getIndustry.map(item => ({
        label: item.title, value: item.id
      }));
      this.fieldMetro.options = this.getMetro.map(item => ({
        label: item.title, value: item.id
      }));
      this.fieldEquipments.options = this.getEquipments.map(item => ({
        label: item.title, value: item.id
      }));
      this.fieldAccessabilities.options = this.getAccessibilities.map(item => ({
        label: item.title, value: item.id
      }));
      this.fieldFacilities.options = this.getFacilities.map(item => ({
        label: item.title, value: item.id
      }));
    },

  components: {
        BaseFormFieldMultiselect,
        FilterFormFieldFromTo
    },
    methods: {
      ...mapActions(["fetchIndustry", "fetchMetro", "fetchAccessibilities", "fetchFacilities", "fetchEquipments"])
    },
    async mounted() {
      await this.fetchIndustry();
      await this.fetchMetro();
      await this.fetchEquipments();
      await this.fetchFacilities();
      await this.fetchAccessibilities();
    },
  computed: {
      ...mapGetters(["getIndustry", "getMetro", "getAccessibilities", "getFacilities", "getEquipments", "getFacilities"])
  }
}
</script>