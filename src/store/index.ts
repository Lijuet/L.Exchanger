import { createStore } from "vuex";
import { moduleURL, ModuleURLState } from "@/store/modules/ModuleURL";
import { moduleUser, ModuleUserState } from "@/store/modules/ModuleUser";

export interface RootState {
  moduleURL: ModuleURLState;
  moduleUser: ModuleUserState;
}

export default createStore({
  modules: {
    moduleURL,
    moduleUser,
  },
});
