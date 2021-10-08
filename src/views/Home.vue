<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <button @click="removeToken">Logout</button>
    <button
      @click="
        autoMatchGroup({
          studyLanguage: this.studyLanguage,
        })
      "
    >
      Auto Matching
    </button>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { mapState, mapMutations, mapActions } from "vuex";

export default defineComponent({
  name: "Home",
  data() {
    return {
      studyLanguage: "ko",
    };
  },
  computed: {
    ...mapState("moduleURL", ["backBaseURL"]),
    ...mapState("moduleUser", ["userEmail"]),
  },
  methods: {
    ...mapMutations("moduleUser", ["removeToken"]),
    ...mapActions("moduleMatch", ["autoMatchGroup"]),
  },
});
</script>
