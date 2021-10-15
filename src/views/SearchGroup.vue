<template>
  <div>Search Group {{ this.$route.query.studyLanguage }}</div>
  <button @click="listGroupSearchResult">Search Group</button>
  {{ this.ableGroups }}
</template>
<script lang="ts">
import store from "@/store";
import { defineComponent } from "vue";

export default defineComponent({
  data() {
    return {
      ableGroups: [],
    };
  },
  methods: {
    async listGroupSearchResult() {
      const result = await store.dispatch("moduleMatch/searchGroup", {
        studyLanguage: this.$route.query.studyLanguage,
      });
      this.ableGroups = JSON.parse(result.data["result"]);
    },
  },
});
</script>
