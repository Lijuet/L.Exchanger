import axios from "axios";
import { VueCookieNext } from "vue-cookie-next";

// Add a request interceptor
axios.interceptors.request.use(
  function (config) {
    config.headers["Authorization"] =
      "Bearer " + VueCookieNext.getCookie("accessToken");
    console.log("axios request intercept : ", config);
    return config;
  },
  function (error) {
    console.log("axios request error : ", error);
    return Promise.reject(error);
  }
);

// Add a response interceptor
axios.interceptors.response.use(
  function (response) {
    // Any status code that lie within the range of 2xx cause this function to trigger
    // Do something with response data
    console.log("axios response intercept : ", response);
    return response;
  },
  function (error) {
    // Any status codes that falls outside the range of 2xx cause this function to trigger
    // Do something with response error
    console.log("axios response error : ", error);
    return Promise.reject(error);
  }
);

// export default axios;
