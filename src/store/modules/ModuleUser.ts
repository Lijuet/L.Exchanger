import { Module } from "vuex";
import { RootState } from "../index";

import { VueCookieNext } from "vue-cookie-next";
import axios from "axios";
import router from "@/router";

export interface ModuleUserState {
  accessToken: string;
  refreshToken: string;
  userID: number;
  userEmail: string;
  userName: string;
  userMainLanguage: string;
}

export const moduleUser: Module<ModuleUserState, RootState> = {
  namespaced: true,
  state: {
    accessToken: "",
    refreshToken: "",
    userID: 0,
    userEmail: "",
    userName: "",
    userMainLanguage: "",
  },
  mutations: {
    setUserInfo(state, payload) {
      state.userID = payload.userID;
      state.userEmail = payload.email;
      state.userName = payload.userName;
      state.userMainLanguage = payload.userMainLangugae;
    },
    setToken(state, payload) {
      VueCookieNext.setCookie("accessToken", payload.accessToken);
      VueCookieNext.setCookie("refreshToken", payload.refreshToken);
      state.accessToken = payload.accessToken;
      state.refreshToken = payload.refreshToken;
    },
    refreshToken(state, payload) {
      VueCookieNext.setCookie("accessToken", payload.accessToken);
      state.accessToken = payload.accessToken;
    },
    removeToken() {
      VueCookieNext.removeCookie("accessToken");
      VueCookieNext.removeCookie("refreshToken");
      location.reload();
    },
  },
  getters: {
    getToken() {
      const accessToken = VueCookieNext.getCookie("accessToken");
      const refreshToken = VueCookieNext.getCookie("refreshToken");
      return {
        accessToken: accessToken,
        refreshToken: refreshToken,
      };
    },
  },
  actions: {
    login: ({ commit, rootState }, data) => {
      return new Promise((resolve, reject) => {
        axios
          .post(
            rootState.moduleURL.backBaseURL + rootState.moduleURL.loginURL,
            { email: data.email, password: data.password }
          )
          .then((res) => {
            console.log(res.data);
            commit("setToken", {
              accessToken: res.data["access"],
              refreshToken: res.data["refresh"],
            });
            commit("setUserInfo", {
              userID: res.data["user_id"],
              userEmail: res.data["email"],
              userName: res.data["username"],
              userMainLanguage: res.data["main_language"],
            });
            router.push({ name: "Home" });
          })
          .catch((err) => {
            alert(err.message);
            reject(err.config.data);
          });
      });
    },
    refreshToken: ({ commit, rootState }) => {
      return new Promise((resolve, reject) => {
        axios
          .post(
            rootState.moduleURL.backBaseURL + rootState.moduleURL.refreshURL,
            { refresh: VueCookieNext.getCookie("refreshToken") }
          )
          .then((res) => {
            commit("refreshToken", { accessToken: res.data["access"] });
            resolve(res.data["refresh"]);
          })
          .catch((err) => {
            reject(err.config.data);
          });
      });
    },
  },
};
