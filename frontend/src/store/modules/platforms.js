import axiosInstance from "@/axios.js";

const state = {
    industry: [],
    metro: [],
    accessibilities: [],
    facilities: [],
    equipments: [],
    searchPlatforms: []
};
const actions = {
    async fetchIndustry(state) {
        try {
            const response = await axiosInstance.get("/api/platforms/industry")
            state.commit("setIndustry", response.data);
        } catch (e) {
            console.log(e);
        }
    },
    async fetchMetro(state) {
        try {
            const response = await axiosInstance.get("/api/platforms/metro")
            state.commit("setMetro", response.data);
        } catch (e) {
            console.log(e);
        }
    },
    async fetchAccessibilities(state) {
        try {
            const response = await axiosInstance.get("/api/platforms/accessibilities")
            state.commit("setAccessibilities", response.data);
        } catch (e) {
            console.log(e);
        }
    },
    async fetchFacilities(state) {
        try {
            const response = await axiosInstance.get("/api/platforms/facilities")
            state.commit("setFacilities", response.data);
        } catch (e) {
            console.log(e);
        }
    },
    async fetchEquipments(state) {
        try {
            const response = await axiosInstance.get("/api/platforms/equipments")
            state.commit("setEquipments", response.data);
        } catch (e) {
            console.log(e);
        }
    },
    async fetchSearchPlatforms(state) {
        try {
            const response = await axiosInstance.get("/api/platforms/search")
            state.commit("setSearchPlatforms", response.data);
        } catch (e) {
            console.log(e);
        }
    },

};
const mutations = {
    setIndustry(state, data) {
        state.industry = data;
    },
    setMetro(state, data) {
        state.metro = data;
    },
    setAccessibilities(state, data) {
        state.accessibilities = data;
    },
    setFacilities(state, data) {
        state.facilities = data;
    },
    setEquipments(state, data) {
        state.equipments = data;
    },
    setSearchPlatforms(state, data) {
        state.searchPlatforms = data;
    }
};
const getters = {
    getIndustry(state) {
        return state.industry;
    },
    getMetro(state) {
        return state.metro;
    },
    getAccessibilities(state) {
        return state.accessibilities;
    },
    getFacilities(state) {
        return state.facilities;
    },
    getEquipments(state) {
        return state.equipments;
    },
    getSearchPlatforms(state) {
        return state.searchPlatforms;
    },
};

export default { state, actions, mutations, getters }
