<template>
  <section class="gradient-form container-fluid img-background">
    <div class="container py-5 h-100">
      <div class="card border-0 p-5">
        <h1>Make your own study group!!</h1>
        <form class="mt-5">
          <div class="mb-5">
            <label for="inputEmail" class="form-label"> Group Name </label>
            <input
              type="text"
              class="form-control"
              id="inputEmail"
              v-model="form.groupName"
              placeholder="Enter group name"
              required
            />
          </div>
          <div class="mb-5">
            <label for="inputStudyLanguages" class="form-label">
              Study Languages
            </label>
            <br />
            <input
              id="inputStudyLanguages"
              type="checkbox"
              v-model="form.studyLanguages"
              value="en"
            />
            English
            <input
              id="inputStudyLanguages"
              type="checkbox"
              v-model="form.studyLanguages"
              value="ko"
            />
            Korean
          </div>
          <button
            class="btn btn-primary border-0 btn-block fa-lg gradient-custom-2"
            type="button"
            @click="makeGroup"
          >
            Submit
          </button>
        </form>
      </div>
    </div>
  </section>
</template>

<script lang="ts">
import store from "@/store";
import { defineComponent } from "vue";

export default defineComponent({
  name: "SignUp",
  data() {
    return {
      form: {
        groupName: "Study Group",
        studyLanguages: [],
      },
    };
  },
  methods: {
    async makeGroup() {
      try {
        const response = await store.dispatch("moduleMatch/makeStudyGroup", {
          form: this.form,
        });

        if (response.status == 200) {
          alert("Making Group Success!");
          this.$router.push({ name: "Home" });
        }
      } catch (err) {
        //   alert("Sign Up Failed! \n => " + err["message"]);
      }
    },
  },
});
</script>
<style>
.gradient-custom-2 {
  /* fallback for old browsers */
  background: #fccb90;

  /* Chrome 10-25, Safari 5.1-6 */
  background: -webkit-linear-gradient(
    to right,
    #ee7724,
    #d8363a,
    #dd3675,
    #b44593
  );

  /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
  background: linear-gradient(to right, #ee7724, #d8363a, #dd3675, #b44593);
}
@media (min-width: 769px) {
  .gradient-custom-2 {
    border-top-right-radius: 0.3rem;
    border-bottom-right-radius: 0.3rem;
  }
}
</style>
