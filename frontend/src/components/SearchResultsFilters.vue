<template>
    <div style="display: flex;">
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
export default {
    name: "SearchResultsCards",

    data() {
        return {
            fieldIndustry: { // Индустрии
                placeholder: "Индустрия",
                options: [
                    { label: "Телерадиовещание и новые медиа", value: "industry1" },
                    { label: "Инду..", value: "industry2" },
                    { label: "Индустрия 3", value: "industry3" },
                    { label: "Индустрия 4", value: "industry4" },
                    { label: "Индустрия 5", value: "industry5" }
                ]
            },
            fieldMetro: { // Станции метро
                placeholder: "Метро",
                options: [
                    { label: "Метро 1", value: "metro1" },
                    { label: "Метро 2", value: "metro2" },
                    { label: "Метро 3", value: "metro3" },
                    { label: "Метро 4", value: "metro4" },
                    { label: "Метро 5", value: "metro5" }
                ]
            },
            fieldEquipments: { // Оборудование
                placeholder: "Оборудование",
                options: [
                    { label: "Оборудование1", value: "equipment1" },
                    { label: "Оборудование 2", value: "equipment2" },
                    { label: "Оборудование 3", value: "equipment3" },
                    { label: "Оборудование 4", value: "equipment4" },
                    { label: "Оборудование 5", value: "equipment5" },
                    { label: "Оборудование 6", value: "equipment6" },
                    { label: "Оборудование 7", value: "equipment7" },
                    { label: "Оборудование 8", value: "equipment8" },
                    { label: "Оборудование 9", value: "equipment9" },
                    { label: "Оборудование 10", value: "equipment10" },
                    { label: "Оборудование 11", value: "equipment11" },
                    { label: "Оборудование 12", value: "equipment12" },
                    { label: "Оборудование 13", value: "equipment13" },
                    { label: "Оборудование 14", value: "equipment14" },
                    { label: "Оборудование 15", value: "equipment15" },
                    { label: "Оборудование 16", value: "equipment16" },
                    { label: "Оборудование 17", value: "equipment17" },
                    { label: "Оборудование 18", value: "equipment18" },
                    { label: "Оборудование 19", value: "equipment19" },
                    { label: "Оборудование 20", value: "equipment20" }
                ]
            },
            fieldAccessabilities: { // Доступность
                placeholder: "Доступность",
                options: [
                    { label: "Доступность 1", value: "accessability1" },
                    { label: "Доступность 2", value: "accessability2" },
                    { label: "Доступность 3", value: "accessability3" },
                    { label: "Доступность 4", value: "accessability4" }
                ]
            },
            fieldFacilities: { // Удобства
                placeholder: "Удобства",
                options: [
                    { label: "Удобство 1", value: "facility1" },
                    { label: "Удобство 2", value: "facility2" },
                    { label: "Удобство 3", value: "facility3" },
                    { label: "Удобство 4", value: "facility4" },
                    { label: "Удобство 5", value: "facility5" }
                ]
            }
        }
    },

    components: {
        BaseFormFieldMultiselect,
        FilterFormFieldFromTo
    }
}
</script>