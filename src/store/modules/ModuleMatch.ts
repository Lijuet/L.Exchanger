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
            resolve(res);
          })
          .catch((err) => {
            reject(err.config.data);
          });
      });
    },
    makeStudyGroup: ({ rootState }, data) => {
      return new Promise((resolve, reject) => {
        axios
          .post(
            rootState.moduleURL.backBaseURL + rootState.moduleURL.studyGroupURL,
            {
              studyLanguages: [
                rootState.moduleUser.userMainLanguage,
                data["studyLanguage"],
              ],
              wishMembers: [
                ...data["wishMembers"],
                rootState.moduleUser.userEmail,
              ],
            }
          )
          .then((res) => {
            console.log(res);
            resolve(res);
          })
          .catch((err) => {
            reject(err.config.data);
          });
      });
    },
  },
};
