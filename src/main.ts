import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "./utils/axios";

import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";

import { VueCookieNext } from "vue-cookie-next";

const app = createApp(App);

app.use(store);
app.use(router);
app.use(VueCookieNext);

app.mount("#app");
