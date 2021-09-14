import { Module } from "vuex";
import { RootState } from "../index";

export interface ModuleURLState {
  backBaseURL: string;
}

export const moduleURL: Module<ModuleURLState, RootState> = {
  namespaced: true,
  state: {
    backBaseURL: "http://localhost:8000",
  },
};
