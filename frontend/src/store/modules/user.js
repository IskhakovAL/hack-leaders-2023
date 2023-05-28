import axiosInstance from "@/axios.js";

const state = {
    isLogin: false,
    user: null
};
const actions = {
    async signUp(state, data) {
      try {
          state.commit("setUser", null);
          const response = await axiosInstance.post("/api/users/register", data);
          let token = response.data.access_token;
          localStorage.setItem("token", token);
          state.commit("setIsLogin", true)
      } catch (error) {
          alert("Сервис работает, кажется вы сделали что-то не так: " + error.response.data.detail)
          console.log(error)
      }
    },
    async signIn(state, data) {
        try {
            state.commit("setUser", null);
            const response = await axiosInstance.post("/api/users/login", data);
            let token = response.data.access_token;
            localStorage.setItem("token", token);
            state.commit("setIsLogin", true);
        } catch (error) {
            alert("Сервис работает, кажется вы сделали что-то не так: " + error.response.data.detail)
            console.log(error);
        }
    },
    async fetchUser(state) {
        try {
            const response = await axiosInstance.get("/api/users/me")
            state.commit("setUser", response.data)
        } catch (error) {
            alert("Сервис работает, кажется вы сделали что-то не так: " + error.response.data.detail)
            console.log(error);
        }
    }
};
const mutations = {
    setIsLogin(state, value) {
        state.isLogin = value;
    },
    setUser(state, value) {
        state.user = value;
    }
};
const getters = {
    getIsLogin(state) {
        return state.isLogin;
    },
    getUser(state) {
        return state.user;
    }
};

export default { state, actions, mutations, getters }
