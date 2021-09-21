<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <button @click="removeToken">Logout</button>
    <button @click="testToken">Get Information</button>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { mapState, mapMutations } from "vuex";
import axios from "axios";

export default defineComponent({
  name: "Home",
  computed: {
    ...mapState("moduleURL", ["backBaseURL"]),
  },
  methods: {
    ...mapMutations("moduleUser", ["removeToken"]),
    async testToken() {
      try {
        const response = await axios({
          method: "GET",
          url: this.backBaseURL + "accounts/",
        });

        if (response.status == 200) {
          console.log("SUCCESS");
          alert(response.data);
        } else alert(response.data["err_msg"]);
      } catch (err) {
        alert("Load Login Information Failed! \n=> " + err.message); // TODO:Pretty Alert
      }
    },
  },
});
</script>
