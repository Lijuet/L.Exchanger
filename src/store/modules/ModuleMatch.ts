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
    autoMatchGroup: ({ rootState }, data) => {
      return new Promise((resolve, reject) => {
        axios
          .post(
            rootState.moduleURL.backBaseURL + rootState.moduleURL.autoMatchURL,
            {
              email: rootState.moduleUser.userEmail,
              studyLanguage: data.studyLanguage,
            }
          )
          .then((res) => {
            console.log(JSON.parse(res.data["result"]));
          })
          .catch((err) => {
            reject(err.config.data);
          });
      });
    },
  },
};
