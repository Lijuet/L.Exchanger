<template>
  <Navbar v-show="!isLogin" />
  <router-view />
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Navbar from "@/views/components/Navbar.vue";

export default defineComponent({
  components: {
    Navbar,
  },
  computed: {
    isLogin(): boolean {
      return this.$route.name === "Login";
    },
  },
});
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
