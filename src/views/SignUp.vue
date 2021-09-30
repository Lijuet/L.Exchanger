<template>
  <div class="container">
    <form>
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
        <label for="inputUsername" class="form-label">Username</label>
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
        <label for="inputPassword" class="form-label">Password</label>
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
          Your password must be 8-20 characters long, contain letters and
          numbers, and must not contain spaces, special characters, or emoji.
        </div>
      </div>

      <div class="mb-3">
        <label for="inputMainLanguage" class="form-label">Main Language</label>
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
        <div id="languageHelpBlock" class="form-text">
          Main language and Study language should be different.
        </div>
      </div>

      <div class="mb-3">
        <label for="inputGoal" class="form-label">Goal for study</label>
        <select id="inputGoal" class="form-select" v-model="form.goal" required>
          <option selected>Select goal</option>
          <option value="conv">Conversation</option>
          <option value="test">Test</option>
        </select>
      </div>

      <a class="btn btn-primary" @click="signUp">Submit</a>
    </form>
  </div>
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
        alert("Sign Up Failed! \n => " + err.message);
      }
    },
  },
});
</script>
