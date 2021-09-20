import { Module } from "vuex";
import { RootState } from "../index";

import { VueCookieNext } from "vue-cookie-next";

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
  actions: {},
};
