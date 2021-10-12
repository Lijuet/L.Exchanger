import { createStore } from "vuex";
import { moduleURL, ModuleURLState } from "@/store/modules/ModuleURL";
import { moduleUser, ModuleUserState } from "@/store/modules/ModuleUser";
import { moduleMatch, ModuleMatchState } from "@/store/modules/ModuleMatch";

import createPersistedState from "vuex-persistedstate";

export interface RootState {
  moduleURL: ModuleURLState;
  moduleUser: ModuleUserState;
  moduleMatch: ModuleMatchState;
}

export default createStore({
  modules: {
    moduleURL,
    moduleUser,
    moduleMatch,
  },
  plugins: [
    createPersistedState({
      paths: ["moduleUser"],
    }),
  ],
});
