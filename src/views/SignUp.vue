<template>
  <section class="gradient-form img-background">
    <div class="container py-5 h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-xl-10">
          <div class="card border-0 rounded-3 text-black">
            <form class="row g-0">
              <div class="col-lg-6">
                <div class="card-body p-md-5">
                  <div class="mb-3">
                    <label for="inputEmail" class="form-label">Email</label>
                    <input
                      type="email"
                      class="form-control"
                      id="inputEmail"
                      v-model="form.email"
                      placeholder="Enter email"
                      aria-describedby="emailHelp"
                      required
                    />
                    <div id="emailHelp" class="form-text">
                      We'll never share your email with anyone else.
                    </div>
                  </div>

                  <div class="mb-3">
                    <label for="inputUsername" class="form-label"
                      >Username</label
                    >
                    <input
                      type="text"
                      class="form-control"
                      id="inputUsername"
                      v-model="form.username"
                      placeholder="Enter username"
                      required
                    />
                  </div>

                  <div class="mb-3">
                    <label for="inputPassword" class="form-label"
                      >Password</label
                    >
                    <input
                      type="password"
                      class="form-control"
                      id="inputPassword"
                      v-model="form.password"
                      placeholder="Enter password"
                      aria-describedby="password-help-block"
                      required
                    />
                    <div id="passwordHelpBlock" class="form-text">
                      Your password must be 8-20 characters long, contain
                      letters and numbers, and must not contain spaces, special
                      characters, or emoji.
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-lg-6 d-flex align-items-center">
                <div class="card-body p-md-5">
                  <div class="mb-3">
                    <label for="inputMainLanguage" class="form-label"
                      >Main Language</label
                    >
                    <select
                      id="inputMainLanguage"
                      class="form-select"
                      v-model="form.main_language"
                      required
                    >
                      <option selected>Select main language</option>
                      <option value="en">English</option>
                      <option value="ko">Korean</option>
                    </select>
                  </div>

                  <div class="mb-3">
                    <label for="inputStudyLanguage" class="form-label">
                      Study Language
                    </label>
                    <select
                      id="inputStudyLanguage"
                      class="form-select"
                      v-model="form.study_language"
                      required
                    >
                      <option selected>Select study language</option>
                      <option value="en">English</option>
                      <option value="ko">Korean</option>
                    </select>
                  </div>

                  <div class="mb-3">
                    <label for="inputGoal" class="form-label"
                      >Goal for study</label
                    >
                    <select
                      id="inputGoal"
                      class="form-select"
                      v-model="form.goal"
                      required
                    >
                      <option selected>Select goal</option>
                      <option value="conv">Conversation</option>
                      <option value="test">Test</option>
                    </select>
                  </div>
                  <button
                    class="
                      btn btn-primary
                      border-0
                      btn-block
                      fa-lg
                      gradient-custom-2
                      mb-3
                    "
                    type="button"
                    @click="signUp"
                  >
                    Submit
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script lang="ts">
import axios from "axios";
import { defineComponent } from "@vue/runtime-core";
import { mapState } from "vuex";

export default defineComponent({
  name: "SignUp",
  data() {
    return {
      form: {
        email: this.email,
        username: "",
        password: "",
        main_language: "Select main language",
        study_language: "Select study language",
        goal: "Select goal",
      },
    };
  },
  computed: {
    ...mapState("moduleURL", ["backBaseURL", "signUpURL"]),
  },
  methods: {
    async signUp() {
      try {
        const response = await axios({
          method: "POST",
          url: this.backBaseURL + this.signUpURL,
          data: this.form,
        });

        if (response.status == 200) {
          alert("Sign Up Success! Go to Login page");
          this.$router.push({ name: "Login" });
        }
      } catch (err) {
        // alert("Sign Up Failed! \n => " + err["message"]);
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
