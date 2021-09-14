import { createStore } from "vuex";
import { moduleURL, ModuleURLState } from "@/store/modules/ModuleURL";
import { moduleUser, ModuleUserState } from "@/store/modules/ModuleUser";

export interface RootState {
  ModuleURL: ModuleURLState;
  ModuleUser: ModuleUserState;
}

export default createStore({
  modules: {
    moduleURL,
    moduleUser,
  },
});
