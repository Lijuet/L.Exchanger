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

      <a align="center" @click="login"> Jump to L.Exchanger </a>
      <p align="center" @click="signup">Sign Up</p>
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
    ...mapState("moduleURL", ["backBaseURL"]),
  },
  methods: {
    ...mapMutations("moduleUser", ["setToken"]),
    async login() {
      try {
        console.log(this.backBaseURL);
        const response = await axios({
          method: "POST",
          url: this.backBaseURL + "/accounts/login/",
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
        }
      } catch (err) {
        alert("Login Failed! \n=> " + err.message); // TODO:Pretty Alert
      }
    },
  },
});
</script>
