<template>
    <div>
        <h1 class="registration__title">Добавить площадку</h1>
        <form class="form" style="margin-top: 16px" @submit.prevent="submit" novalidate>
            <div class="form__column form__column_size_l">
                <places-add-form-field-title v-model="form.title" :v="$v.form.title" />
                <places-add-form-field-address v-model="form.address" :v="$v.form.address" />
                <places-add-form-field-description v-model="form.description" :v="$v.form.description" />
                <BaseFormFieldMultiselectL :field="fieldIndustry" />
                <BaseFormFieldMultiselectL :field="fieldMetro" />
                <places-add-form-field-square v-model="form.square" :v="$v.form.square" />
            </div>
            <div class="form__column form__column_size_l">
                <BaseFormFieldMultiselectL class="multiselect_size_l" :field="fieldEquipments" />
                <BaseFormFieldMultiselectL :field="fieldAccessabilities" />
                <signup-form-field-phone v-model="form.phone" :v="$v.form.phone" />
                <BaseFormFieldMultiselectL :field="fieldFacilities" />
                <div class="field-from-to field-from-to_size_l">
                    <div class="field-from-to__title field-from-to__title_size_l">Количество человек</div>
                    <input class="field-from-to__field field-from-to__field_size_l" type="number" min="1" placeholder="От">
                    <input class="field-from-to__field field-from-to__field_size_l" type="number" max="1000" placeholder="До">
                </div>
            </div>
            <div class="form__column" style="width: 275px;">
                <div class="field-from-to field-from-to_size_l">
                    <div class="field-from-to__title field-from-to__title_size_l">Временные слоты</div>
                    <input class="field-from-to__field field-from-to__field_size_l" type="date" :min="getTodayDate" placeholder="От">
                    <input class="field-from-to__field field-from-to__field_size_l" type="date" :min="getTodayDate" placeholder="До">
                </div>
                <!-- photo -->
                <img src="../assets/add-photo-button.svg" alt="">
                <button class="button button_size_m button_color_pink" type="submit" :disabled="this.$v.$invalid">Добавить</button>
            </div>
        </form>
    </div>
</template>

<script>
import { required } from "vuelidate/lib/validators";
import { isPhoneEntered } from "@/validators";
import PlacesAddFormFieldTitle from "./PlacesAddFormFieldTitle.vue";
import PlacesAddFormFieldAddress from "./PlacesAddFormFieldAddress.vue";
import PlacesAddFormFieldDescription from "./PlacesAddFormFieldDescription.vue";
import PlacesAddFormFieldSquare from "./PlacesAddFormFieldSquare.vue";
import SignupFormFieldPhone from "./SignupFormFieldPhone.vue";
import BaseFormFieldMultiselectL from "@/components/BaseFormFieldMultiselectL.vue";

export default {
    name: "PlacesAddForm",

    components: {
        PlacesAddFormFieldTitle,
        PlacesAddFormFieldAddress,
        PlacesAddFormFieldDescription,
        PlacesAddFormFieldSquare,
        SignupFormFieldPhone,
        BaseFormFieldMultiselectL
    },

    data() {
        return {
            form: {
                title: "",
                address: "",
                description: "",
                square: "",
                phone: ""
            },
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
                    { label: "Оборудование 1", value: "equipment1" },
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
        };
    },

    validations: {
        form: {
            title: { required },
            address: { required },
            description: { required },
            square: { required },
            phone: { required, isPhoneEntered }
        }
    },

    methods: {
        getTodayDate() {
            var d = new Date();
            var day = d.getDate();
            if (day < 10) {
                day = '0' + day;
            }
            var month = d.getMonth() + 1;
            if (month < 10) {
                month = '0' + month;
            }
            var year = d.getFullYear();
            return (year + "-" + month + "-" + day);
        },
    }
};
</script>

<style scoped>
.field-from-to__title_size_l {
    height: 32px;
    font-size: 16px; 
    line-height: 20px;
}

.field-from-to__field_size_l {
    width: 50%; 
    height: 32px; 
    font-size: 16px; 
    line-height: 20px;
}

.field-from-to__field_size_l::placeholder {
    font-size: 16px; 
    line-height: 20px;
}

.field-from-to__field_size_l::-webkit-input-placeholder {
    font-size: 16px; 
    line-height: 20px;
}

.field-from-to__field_size_l::-moz-placeholder {
    font-size: 16px; 
    line-height: 20px;
}

.field-from-to__field_size_l::-ms-input-placeholder {
    font-size: 16px; 
    line-height: 20px;
}
</style>
  