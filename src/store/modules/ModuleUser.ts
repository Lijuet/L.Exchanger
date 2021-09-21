import { Module } from "vuex";
import { RootState } from "../index";

import { VueCookieNext } from "vue-cookie-next";
import axios from "axios";

export interface ModuleUserState {
  accessToken: string;
  refreshToken: string;
}

export const moduleUser: Module<ModuleUserState, RootState> = {
  namespaced: true,
  state: {
    accessToken: "",
    refreshToken: "",
  },
  mutations: {
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
    refreshToken: ({ commit, rootState }) => {
      console.log("Refresh Token Actions : " + rootState.moduleURL.backBaseURL);
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
            console.log("Refresh Action Error : " + err);
            reject(err.config.data);
          });
      });
    },
  },
};
