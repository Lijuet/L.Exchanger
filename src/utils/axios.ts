import store from "@/store";
import axios from "axios";
import { VueCookieNext } from "vue-cookie-next";

// Add a request interceptor
axios.interceptors.request.use(
  function (config) {
    if (
      config.url != "http://localhost:8000/accounts/login/" &&
      config.url != "http://localhost:8000/accounts/signup/"
    )
      config.headers["Authorization"] =
        "Bearer " + VueCookieNext.getCookie("accessToken");
    return config;
  },
  function (err) {
    return Promise.reject(err);
  }
);

// Add a response interceptor
axios.interceptors.response.use(
  function (response) {
    try {
      return response;
    } catch (err) {
      console.error("[axios.interceptors.response] error : ", err);
    }
  },
  async function (err) {
    // Any status codes that falls outside the range of 2xx cause this function to trigger
    // Do something with response err
    try {
      const errorAPI = err.response.config;
      if (
        err.response.status == 401 &&
        VueCookieNext.getCookie("refreshToken") != null
      ) {
        await store.dispatch("moduleUser/refreshToken");
        return await axios(errorAPI);
      }
    } catch (err) {
      // console.log("[axios.interceptors.response] refresh error : ", err);
    }
    return Promise.reject(err);
  }
);

// export default axios;
