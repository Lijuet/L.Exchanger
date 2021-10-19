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
  font-family: NeoDunggeunmo, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

@font-face {
  font-family: "NeoDunggeunmo";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.3/NeoDunggeunmo.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
</style>
