<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <button @click="removeToken">Logout</button>
    <button @click="autoMatchGroup">Auto Matching</button>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { mapState, mapMutations, mapActions } from "vuex";

export default defineComponent({
  name: "Home",
  computed: {
    ...mapState("moduleURL", ["backBaseURL"]),
  },
  methods: {
    ...mapMutations("moduleUser", ["removeToken"]),
    ...mapActions("moduleMatch", ["autoMatchGroup"]),
  },
});
</script>
