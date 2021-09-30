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

      <a align="center" @click="login">Jump to L.Exchanger</a>
      <button align="center" @click="signup">Sign Up</button>
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { mapState, mapMutations } from "vuex";
import axios from "axios";

export default defineComponent({
  name: "Login",
  data() {
    return {
      email: "",
      password: "",
    };
  },
  computed: {
    ...mapState("moduleURL", ["backBaseURL", "loginURL"]),
  },
  methods: {
    ...mapMutations("moduleUser", ["setToken"]),
    async login() {
      try {
        const response = await axios({
          method: "POST",
          url: this.backBaseURL + this.loginURL,
          data: {
            email: this.email,
            password: this.password,
          },
        });
        if (response.status == 200) {
          this.setToken({
            accessToken: response.data["access"],
            refreshToken: response.data["refresh"],
          });
          this.$router.push({ name: "Home" });
        } else alert(response.data["err_msg"]);
      } catch (err) {
        alert("Login Failed! \n=> " + err.message); // TODO:Pretty Alert
      }
    },
    signup() {
      this.$router.push({ name: "SignUp" });
    },
  },
});
</script>
