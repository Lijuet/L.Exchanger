import { Module } from "vuex";
import { RootState } from "../index";

import axios from "axios";

export interface ModuleMatchState {
  isRecruiting: boolean;
}

export const moduleMatch: Module<ModuleMatchState, RootState> = {
  namespaced: true,
  state: {
    isRecruiting: true,
  },
  getters: {},
  mutations: {},
  actions: {
    autoMatchGroup: ({ rootState }) => {
      return new Promise((resolve, reject) => {
        axios
          .get(
            rootState.moduleURL.backBaseURL + rootState.moduleURL.autoMatchURL
          )
          .then((res) => {
            console.log(res.data);
          })
          .catch((err) => {
            reject(err.config.data);
          });
      });
    },
  },
};
