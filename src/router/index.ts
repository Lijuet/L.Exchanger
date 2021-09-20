import store from "@/store";
import { VueCookieNext } from "vue-cookie-next";
import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import Home from "../views/Home.vue";
import Login from "../views/Login.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach(async (to, from, next) => {
  if (
    VueCookieNext.getCookie("accessToken") === null &&
    VueCookieNext.getCookie("refreshToken") !== null
  ) {
    await store.dispatch("refreshToken");
  }
  if (to.name == "Login" || VueCookieNext.getCookie("accessToken"))
    return next();
  else if (
    VueCookieNext.getCookie("accessToken") === null &&
    VueCookieNext.getCookie("refreshToken") === null
  ) {
    return next({ name: "Login" });
  } else return next();
});

export default router;
