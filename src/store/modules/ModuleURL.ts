import { Module } from "vuex";
import { RootState } from "../index";

export interface ModuleURLState {
  backBaseURL: string;
  refreshURL: string;
  loginURL: string;
  signUpURL: string;
  autoMatchURL: string;
}

export const moduleURL: Module<ModuleURLState, RootState> = {
  namespaced: true,
  state: {
    backBaseURL: "http://localhost:8000/",
    refreshURL: "accounts/api/token/refresh/",
    loginURL: "accounts/login/",
    signUpURL: "accounts/signup/",
    autoMatchURL: "groups/autoMatch/",
  },
};
