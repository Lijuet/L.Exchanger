<template>
  <div class="Login">Login Page</div>
  <div>
    <form>
      <input
        class="email"
        v-model="email"
        type="email"
        align="center"
        placeholder="Email"
      />
      <input
        class="pwd"
        v-model="password"
        type="password"
        align="center"
        placeholder="Password"
      />

      <a
        align="center"
        @click="login({ email: this.email, password: this.password })"
        >Jump to L.Exchanger</a
      >
      <button align="center" @click="signup">Sign Up</button>
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { mapState, mapMutations, mapActions } from "vuex";
import axios from "axios";

export default defineComponent({
  name: "Login",
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    ...mapActions("moduleUser", ["login"]),
    signup() {
      this.$router.push({ name: "SignUp" });
    },
  },
});
</script>
