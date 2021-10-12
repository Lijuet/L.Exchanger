<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <button @click="removeToken">Logout</button>
    <button @click="listAutoMatchResult">Auto Matching</button>
    <div>
      <div v-for="(member, key) in ableMembers" :key="key">
        <input
          type="checkbox"
          :id="member.email"
          :value="member.email"
          v-model="wishMembers"
        />
        <label :for="member.email">{{ member }}</label>
      </div>
      <button
        @click="
          makeStudyGroup({
            wishMembers: wishMembers,
            studyLanguage: this.studyLanguage,
          })
        "
      >
        Make Study Group
      </button>
      <span>Checked email: {{ wishMembers }}</span>
    </div>
  </div>
</template>

<script lang="ts">
import store from "@/store";
import { defineComponent } from "vue";
import { mapState, mapMutations, mapActions } from "vuex";
// const store = useStore();

export default defineComponent({
  name: "Home",
  data() {
    return {
      studyLanguage: "ko",
      ableMembers: [],
      wishMembers: [],
    };
  },
  computed: {
    ...mapState("moduleURL", ["backBaseURL"]),
    ...mapState("moduleUser", ["userEmail"]),
  },
  methods: {
    ...mapMutations("moduleUser", ["removeToken"]),
    ...mapActions("moduleMatch", ["makeStudyGroup"]),
    async listAutoMatchResult() {
      const result = await store.dispatch("moduleMatch/autoMatchGroup", {
        studyLanguage: this.studyLanguage,
      });
      this.ableMembers = JSON.parse(result.data["result"]);
    },
  },
});
</script>
