import axiosInstance from "@/axios.js";

const state = {
    isLogin: false
};
const actions = {
    async signin(state, data) {
        try {
            const response = await axiosInstance.post("api/users/login", data);
            let token = response.data.access_token;
            localStorage.setItem("token", token);
            state.commit("setIsLogin", true);
        } catch {
            console.log("error");
        }
    }
};
const mutations = {
    setIsLogin(state, value) {
        state.isLogin = value;
    }
};
const getters = {
    getIsLogin(state) {
        return state.isLogin;
    }
};

export default { state, actions, mutations, getters }
