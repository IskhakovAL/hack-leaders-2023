import axios from "axios";

const axiosInstance = axios.create({
    baseURL: "http://178.170.197.108",
});

axiosInstance.interceptors.request.use(function (config) {
    // Do something before request is sent
    let token = localStorage.getItem("token");
    config.headers["Authorization"] = "Bearer " + token;
    return config;
});

export default axiosInstance;